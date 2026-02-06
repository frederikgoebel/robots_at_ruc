# Universal Robot Documentation & Code

This repository contains documentation and code to work with the Universal Robot UR5e at the Roskilde University.
The repository is still being developed, currently only a few hints and and a code sample for real time control are provided


# Documentation

## Links
[Real time docs](https://docs.universal-robots.com/tutorials/communication-protocol-tutorials/rtde-guide.html) 

[End effector I/Os](https://www.universal-robots.com/manuals/EN/HTML/SW5_21/Content/prod-usr-man/complianceUR30/SW_sections/first_program/io_tool.htm)

[Datasheet](https://www.universal-robots.com/media/1807465/ur5e_e-series_datasheets_web.pdf)

[Simulator](https://docs.universal-robots.com/Universal_Robots_ROS_Documentation/doc/ur_client_library/doc/setup/ursim_docker.html)

## Remote Control

### Test
1. Connect computer via ethernet cable
2. Make sure that the network settings are set to DHCP on your computer
3. Try to connect to the robot:
4. type the following in a terminal / command line: ```ping 10.0.0.4```

> [!NOTE]
> On macOS make sure to allow the terminal or your program to access the local network:
> ```System Settings -> Privacy & Security -> Local Network: <Enable for your program> ```

### Troubleshooting

### Check IP

   1. On the robot interface click on the hamburger menu in the top right corner
   2. Click ```Info```
   3. See ```IP Address```
   4. If the IP is set and it shows ```connected```try to use that IP to ping the robot. 

### Disable other networks
The IP range of the router connected to the robot should not yield public IP addresses but to double check disable WIFI and other network connections.

### Dashboard Server (not actually a GUI)
Once a simple ping to the robot is working you can access the RemoteDashboard API by running the following command:
```nc 10.0.0.4 29999```

Afterwards commands can be send from the running session.

Available commands can be found [here](https://s3-eu-west-1.amazonaws.com/ur-support-site/42728/DashboardServer_e-Series_2022.pdf).

### Real Time Data Exchange (RTDE)

[Docs](https://docs.universal-robots.com/tutorials/communication-protocol-tutorials/rtde-guide.html)


### Remote uploading of files

1. Download Filezilla
2. In Filezilla connect with:
```
IP: 10.0.0.4 or IP of robot
User: root
Password: <password is in the robot controller box>
Port: 22
```
3. Move program files into the ```/programs/``` directory.
4. On the robot, load the program by going to ```Program->Open...-> Program```

> [!CAUTION]
> Only upload, change or delete files in the ```/programs``` directory!
> Removing other files might break the robot.

[Docs](https://docs.universal-robots.com/tutorials/urscript-tutorials/ftp.html)

## Running the Simulator

> [!WARNING]
> By default the docker image does not forward all the ports of the controller. This means that the above mentioned remote connections do not currently work with the simulator. (Someone might want to figure this out)

1. Install docker (or orbstack)
2. Run command from the guide:
```docker run --rm -it -p 5900:5900 -p 6080:6080 --name ursim universalrobots/ursim_e-series```
3. Go to web interface, address is printed by command


# Software

## RTDE-Websocket-Bridge

The folder ```rtde_ws_bridge```containts a python server that interpets websocket data and converts these into the appropriate format for tcop connection to the robot. 

The project uses [UV](https://github.com/astral-sh/uv) as a package manager. Make sure to install it first.  Afterwards run:

```uv run main.py --help```

With the default IP of the robot the program can be started as:

```uv run main.py```

The websocket will be exposed on ```0.0.0.0:8765```.

An example of a p5 sketch sending position updates and reading out the force on the arm can be found in the file ```example_p5.js```.

On the robot run the program ```XXX-whats the name``` to receive realtime positions and execute movements. 

// TODO more documentation


# Misc
 [Video series about real time control](https://www.youtube.com/watch?v=N2nh3iG7kvo)

Might be worth checking out, there is a js repo: https://github.com/RobotExMachina

We might want to look into this library: https://www.robotexchange.io/t/how-to-control-a-ur-robot-from-python-using-rtde/3271