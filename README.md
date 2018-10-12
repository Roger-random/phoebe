# ROS Package For Phoebe TurtleBot
This is a software package for running ROS ([Robot Operating System](http://www.ros.org/))
on [Phoebe. Phoebe](https://hackaday.io/project/161085-phoebe-turtlebot)
is a DIY variant of [TurtleBot](https://www.turtlebot.com/), the introductory hardware platform for ROS. Like the TurtleBots, Phoebe has a small onboard computer (Raspberry Pi 3) that can handle some ROS tasks, but there are
robot tasks that require heavy computation beyond what the onboard computer can handle. Such tasks must be offloaded to a more powerful computer
operating on the same network.

Phoebe leverages the extensive ROS component ecosystem for functionality,
as a result there is almost no source code in this repository. Most of the
files here composes open source ROS modules together to run Phoebe.

# Phoebe Capabilities
* Human operation by joystick/gamepad.
(Drive around like a remote control car.)
* Simultaneous location and mapping
([SLAM](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping))
using [GMapping](http://wiki.ros.org/gmapping). This
typically requires assistance from a more powerful computer.
* Autonomous navigation using the [ROS Navigation stack](http://wiki.ros.org/navigation).

Current status: Phoebe is capable of the above, but at the moment
only crudely. There is a great deal of room for improvement in tuning
system parameters for better performance.

# Directory Structure
* __launch__ - collection of files for running `roslaunch`
  * `chassis.launch` - ROS nodes to interface with chassis hardware.
  (Launch onboard Raspberry Pi.)
  * `gmapping.launch` - Launch ROS GMapping SLAM node.
  (Launch on networked, more powerful computer.)
  * `joystick.launch` - Launch ROS joystick control node.
  (Launch on networked computer with attached joystick.)
  * `move_base.launch` - Launch ROS Navigation stack.
  (Can be run onboard for simple maps.)
  * `rviz_gmapping.launch` - Launch RViz to visualize GMapping in progress.
  (Launch on networked computer with screen.)
  * `rviz_nav2d.launch` - Launch RViz to visualize navigation in progress.
  (Launch on networked computer with screen.)
* __nav2d__ - configuration files for ROS navigation. Mostly copied from
[this section](http://wiki.ros.org/navigation/Tutorials/RobotSetup#Navigation_Stack_Setup)
of ROS tutorial with minor modifications described [here](https://newscrewdriver.com/2018/10/11/navigation-stack-setup-for-phoebe/).
* __rviz__ - Configuration files for RViz, the ROS Visualization tool. Used
by `rviz_*.launch` files in the __launch__ subdirectory.
* __scripts__ - Hard coded transform for debugging purposes, not typically used.
  * `baseneato.py` - Publish a fixed transform to relate Neato LIDAR to
  robot base link. Used to isolate whether a problem is due to misconfigured
  robot state publisher and/or URDF bugs.
  * `mapodom.py` - Publish a fixed transform to relate map frame to
  odometry frame. Used to isolate whether a problem is due to misconfigured
  localization algorithm.
* __urdf__ - A simplified geometry description of Phoebe in
[URDF format](http://wiki.ros.org/urdf/Tutorials),
used for RViz visualization and for publishing robot state transforms.

# Launching Tasks
'on Phoebe' means launching on Phoebe's onboard Raspberry Pi 3

'on PC' means launching on a computer on the same network as Phoebe.

One of the two need to be running [`roscore`](http://wiki.ros.org/roscore)
and the two computers need to be in communication via ROS_MASTER_URI, ROS_IP,
[and related parameters](http://wiki.ros.org/ROS/EnvironmentVariables#ROS_MASTER_URI).

* Human operation (drive like a remote control car)
  * Launch `chassis.launch` on Phoebe
  * Launch `joystick.launch` on PC
* Human-directed SLAM with GMapping
  * Launch `chassis.launch` on Phoebe
  * Launch `joystick.launch` on PC
  * Launch `gmapping.launch` on PC
  * (Optional) Launch `rviz_gmapping.launch` on PC
* Autonomous navigation
  * Launch `chassis.launch` on Phoebe
  * Launch [map server](http://wiki.ros.org/map_server)
  * Launch [amcl](http://wiki.ros.org/amcl)
  * Launch `move_base.launch`
  * (Optional) Launch `rviz_nav2d.launch` on PC

# Additional Resources
* Phoebe project page on [Hackaday.io](https://hackaday.io/project/161085-phoebe-turtlebot).
* CAD file for 3D-printed components as [Onshape public document](https://cad.onshape.com/documents/d8642f502d804241234ba911/w/5e720270c0953acbe7b81f82/e/0bd4a7df461cfb87af1b0063).
* Personal [blog entries](https://newscrewdriver.com/category/projects/phoebe-turtlebot/) on Phoebe.
