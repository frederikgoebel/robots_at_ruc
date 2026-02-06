#!/usr/bin/env python
import asyncio
import json
import logging
from queue import Empty
import sys
import argparse

from websockets.asyncio.server import serve
import websockets

sys.path.append("../")
import rtde.rtde as rtde
import rtde.rtde_config as rtde_config

shutdown = asyncio.Event()
target_pos = None

def rtde_state_to_dict(state):
    return {k: v for k, v in state.__dict__.items() if not k.startswith("_")}

def json_safe(obj):
    if isinstance(obj, (int, float, str, bool)) or obj is None:
        return obj
    if isinstance(obj, (list, tuple)):
        return [json_safe(x) for x in obj]
    if isinstance(obj, dict):
        return {k: json_safe(v) for k, v in obj.items()}
    return str(obj)


def list_to_setp(sp, lst):
    for i in range(6):
        setattr(sp, f"input_double_register_{i}", lst[i])
    return sp

async def websocket_handler(websocket, output_queue):
    async def receiver():
        global target_pos
        try:
            async for message in websocket:
                target_pos = json.loads(message)
                logging.debug(f"received <<< {target_pos}")
        except websockets.ConnectionClosed:
            logging.info("WebSocket connection closed (receiver).")

    async def sender():
        try:
            while True:
                state = await output_queue.get()
                serialized = json.dumps(json_safe(rtde_state_to_dict(state)))
                await websocket.send(serialized)
                logging.debug("sent >>> state")
        except websockets.ConnectionClosed:
            logging.info("WebSocket connection closed (sender).")

    recv_task = asyncio.create_task(receiver())
    send_task = asyncio.create_task(sender())

    done, pending = await asyncio.wait(
        {recv_task, send_task},
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        task.cancel()


async def websocket_main(port,output_queue):
    async def handler(websocket):  
        await websocket_handler(websocket, output_queue)

    async with serve(handler, "0.0.0.0", port):
        logging.info(f"WebSocket server running on ws://0.0.0.0:{port}")
        await shutdown.wait() 

async def control_loop_main(robot_host, robot_port, config_file, output_queue):
    conf = rtde_config.ConfigFile(config_file)
    state_names, state_types = conf.get_recipe("state")
    setp_names, setp_types = conf.get_recipe("setp")

    con = rtde.RTDE(robot_host, robot_port)
    try:
        con.connect()
    except:
        logging.error(f"Failed to connect to RTDE server at {robot_host}:{robot_port}")
        shutdown.set()  
        return -1
    major, minor, bugfix, build = con.get_controller_version()
    logging.info(f"Connected to RTDE server at {robot_host}:{robot_port} (Controller version: {major}.{minor}.{bugfix}, build {build})")

    con.send_output_setup(state_names, state_types)
    setp = con.send_input_setup(setp_names, setp_types)

    list_to_setp(setp, [0,0,0,0,0,0])  

    if not con.send_start():
        logging.error("Failed to start RTDE synchronization.")
        return

    loop = asyncio.get_running_loop()
    while True:
        state = await loop.run_in_executor(None, con.receive)
        if state is None:
            break
        
        await output_queue.put(state)  
        if target_pos is not None:
            logging.info(f"New pose = {target_pos}")
            list_to_setp(setp, target_pos)
            con.send(setp)

    con.send_pause()
    con.disconnect()

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--robot_ip", default="10.0.0.4", help="IP of robot (10.0.0.4)"
    )
    parser.add_argument("--robot_port", type=int, default=30004, help="Port of the robot (30004)")

    parser.add_argument(
        "--config",
        default="control_loop_configuration.xml",
        help="data configuration file to use (control_loop_configuration.xml)",
    )
    parser.add_argument("--ws_port", type=int, default=8765, help="Port of the websocket connection (8765)")
    parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:       
        logging.basicConfig(level=logging.INFO)

    logging.info("Running RTDE-Bridge [WebSocket]")
    output_queue = asyncio.Queue()

    websocket_task = asyncio.create_task(websocket_main(args.ws_port, output_queue))
    control_task = asyncio.create_task(control_loop_main(args.robot_ip, args.robot_port, args.config, output_queue))

    await asyncio.gather(websocket_task, control_task)

if __name__ == "__main__":
    asyncio.run(main())
