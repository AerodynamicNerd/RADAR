# RADAR

A Perceptin Radar is used on a Donkey Car. This file extracts all the data from the sensor using Kvaser CAN cables.

Steps:

1. install the linuxcan package # helps extract CAN messages in a linux environment, 

2. launch the master node using "roslaunch kvaser_interfrace kvaser_can_bridge.launch"

3. run the publisher file # The current version only provides the the raw values converted. You might have to build the algorithm. however feel free to reachout for additional information
