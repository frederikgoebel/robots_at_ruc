# Universal Robot UR5e - Documentation & Code

This repository contains documentation and code to work with the Universal Robot UR5e at the Roskilde University.
The repository is still being developed.

# Safety

> [!CAUTION]
> This robot is dangerous if missused! 
>
> Read the following text.

The UR5e is a cobot, this means that it is more safe then a normal industrial robot. When running with the safest settings it will stop on collision. But if missused by attaching dangerous tools, overwriting the speed settings or not fixing it in place it can still hurt you. Therefore be aware of the robot movements and do not stay in the work area of the robot.

## Rules 

1. Be aware of the robot movements. Do not stand in its working envelope.
2. Do not lean under the robot arm.
3. Always have a line of sight to the robot when you run it.  
4. Run programs as `Simulation` (toggle bottom right) before you run them live

# Usage
Save all your `programs` and `installations` in a directory with your RUC username, do not change `programs` or `installations` in other directories:

1. `Save` -> `Save Program As...`
2. `New folder` (icon on top left)
3. `Long press` on folder -> `Rename`
4. Tap on your folder to go into it
5. Enter file name -> `Save`
6. `Save` -> `Save Installation As...`
7. Tap on your folder to go into it
8. Enter installation name -> `Save`
9. If asked: Confirm `Update program`

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

#### Check that robot is started
Make sure the robot, not just the remote, is started. 
1. Lower left corner should be green. Otherwise tap the corner. 
2. Tap ```On```
3. Tap ```Start```

#### Check IP

   1. On the robot interface click on the hamburger menu in the top right corner
   2. Click ```Info```
   3. See ```IP Address```
   4. If the IP is set and it shows ```connected```try to use that IP to ping the robot. 

#### Disable other networks
The IP range of the router connected to the robot should not yield public IP addresses but to double check disable WIFI and other network connections.

### Dashboard Server (not actually a GUI)
Once a simple ping to the robot is working you can access the RemoteDashboard API by running the following command:
```nc 10.0.0.4 29999```

Afterwards commands can be send from the running session.

Available commands can be found [here](https://s3-eu-west-1.amazonaws.com/ur-support-site/42728/DashboardServer_e-Series_2022.pdf).

### Real Time Data Exchange (RTDE)

To stream instructions to and receive information from the robot the Real Time Data Exchange can be used. Read the docs and look at the RTDE-Websocket-Bridge further down. 

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

1. Install docker (or orbstack)
2. Run this command from the root of the project:
```docker run --rm -it -v "./programs:/ursim/programs" -p 5900:5900 -p 6080:6080 --name ursim universalrobots/ursim_e-series -e ROBOT_MODEL=UR5e```
3. Go to web interface, address is printed by command ```http://<IP:PORT>/vnc.html?host=<IP>&port=<PORT>```
4. Confirm safety settings, do general setup, start the virtual robot
5. The remote connections can be used with the simulator

# Software

## RTDE-Websocket-Bridge

The folder ```rtde_ws_bridge```containts a python server that interpets websocket data and converts these into the appropriate format for the tcp connection to the robot. Check the contained readme for more information.


# Misc
 [Video series about real time control](https://www.youtube.com/watch?v=N2nh3iG7kvo)

Might be worth checking out, there is a js repo: https://github.com/RobotExMachina

This as well: https://www.robotexchange.io/t/how-to-control-a-ur-robot-from-python-using-rtde/3271