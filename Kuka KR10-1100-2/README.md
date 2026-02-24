# KUKA KR10-1100-2 - Documentation & Code

This repository contains documentation and code to work with the Kuka KR10-1100-2 at the Roskilde University.
The repository is still being developed.

# Safety

> [!CAUTION]
> This robot is dangerous! 
>
> Read the following text.

The KUKA KR10-1100-2 is an industrial robot, it is made for high payloads and speeds but not safety. It has no functionality or sensor to stop when a person is near. Therefore, do not enter the safety region while it is operating. 

The safety region is secured by a light fence / lidar (xxx-todo). These sensor will emergency stop the robot when someone or something enters the safety region. 

## Rules 

1. Never stand in the range of the robot while it is operating.
2. Do not lean under the robot arm.
3. Only run in automatic mode if you got a safety introduction from a teacher and the ok from them. 
4. Always test your programs in xxx-T1?! before running in automatic mode.
5. Before approaching the robot, for example to change the toolhead, make sure the robot is not moving. And the e-stop on the control board is pressed in. 


# Documentation

## Grasshopper

[Rhino](https://www.rhino3d.com/) and its node based programming evnironment [Grasshopper](https://discourse.mcneel.com/c/grasshopper/2) can be used to generate toolpaths for the robot. 

### KUKA|prc

The Grasshopper library [Kuka|prc](https://www.food4rhino.com/en/app/kukaprc-parametric-robot-control-grasshopper) by [Robots in Architecture](https://robotsinarchitecture.com/) is especially helpful in generating the KRL code and simulationg the robots path. 
More info can be found [here](https://robotsinarchitecture.com/kuka-prc/).


Follow the [installation instructions](https://prc.robotsinarchitecture.org/getting-started/installation). Note that the macOS installation is a bit more convoluted than the Windows installation.

For the license key and possibility of a macOS version contact a responsible person.
