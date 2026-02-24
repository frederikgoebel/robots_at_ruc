# RTDE-WS-Bridge

## Requirements

The project uses [UV](https://github.com/astral-sh/uv) as a package manager. Make sure to install it first. This guide assumes it is installed. 

Otherwise install the required dependencies globally in your python and run it via the normal python interpreter. The dependencies can be found in ```pyproject.toml -> dependencies```(This is not recommended)

## Running

To test :

```uv run main.py --help```

With the default IP of the robot the program can be started as:

```uv run main.py```

The websocket will be exposed on ```0.0.0.0:8765```.

An example of a p5 sketch sending position updates and reading out the force on the arm can be found in the file ```example_p5.js```.

On the robot run the program ```realtime_control.urp``` to receive realtime positions and execute movements.
If the program is not yet uploaded on the robot, use FileZilla to upload the program from the ```programs``` folder to the ```programs```folder on the robot. 
You might want to play with the settings of the ```servoj(...)``` command. Documentation for it can be found [here](https://www.universal-robots.com/articles/ur/programming/servoj-command/).

The current setup looks as following:

![Current setup](../../imgs/setup.png)

### To run the example
1. Conenct ethernet cable to computer
2. Run rtde_ws_bridge ```uv run main.py```
3. Open a p5 sketch, copy past the ```example_p5.js``` code into it.
4. Run the p5 sketch
5. Run the ```realtime_control.urp``` on the robot to start receive position updates
6. Move th mouse in the p5 sketch