#!/usr/bin/env python

import rospy
from can_msgs.msg import Frame 
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
import os

h = []

def callback(data):
    byte_0 = (ord(data.data[0]))
    byte_1 = (ord(data.data[1]))
    byte_2 = (ord(data.data[2]))
    byte_3 = (ord(data.data[3]))
    byte_4 = (ord(data.data[4]))
    byte_5 = (ord(data.data[5]))
    byte_6 = (ord(data.data[6]))
    byte_7 = (ord(data.data[7]))
    
## Radial Range
    g = int(format(byte_1,'08b')[1:8],2)  
    RAW_Range = (int(((g) << 8)+byte_0))
    Radial_Range = (int(RAW_Range) * 0.01) + 0
    #print "point 1"

## Radial Speed
    a = int(format(byte_3,'08b')[2:8],2)  
    RAW_Speed = (int(a) << 8)+ int(byte_2)
    Radial_Speed = (int(RAW_Speed) * 0.01) + 0
    if Radial_Speed >= 81.91:
       Radial_Speed = Radial_Speed - 163.83
     #print "point 2"

## Radial Acceleration
    b = int(format(byte_5,'08b')[6:8],2)
    RAW_Acceleration = (int(b) << 8)+ int(byte_4)
    Radial_Acceleration = (int(RAW_Acceleration) * 0.05) + 0
    if Radial_Acceleration >= 25.22:
       Radial_Acceleration = Radial_Acceleration - 51.1
      #print "point 3"

## Angle
    c =int(format(byte_6,'08b')[3:8],2)
    d =int(format(byte_5,'08b')[0:6],2) 
    RAW_Angle = ((c) << 6)+ (d)
    Angle = (int(RAW_Angle) * 0.1) + 0
    if Angle >= 102.3:
       Angle = Angle - 204.8
      #print "point 4"

## Power
    e = int(format(byte_7,'08b')[1:8],2)
    f = int(format(byte_6,'08b')[0:3],2)
    RAW_Power = (int(e) << 3)+ int(f)
    Power = (int(RAW_Power) * 0.1) - 40
    if Power >= 11.1:
       Power = Power - 102.3
      #print "point 5"
    #print data.id, Radial_Range,"m", Radial_Speed,"m/s", Radial_Acceleration,"m/s2", Angle,"degrees", Power,"dBm"

   
    if data.id < 1343: h.append(Radial_Range)
    else: 
       print h
       os.system('clear')
       del h[:]

    #print Radial_Range
    # if data.id == 1343:
    #   os.system('clear')
    #   del h[:]'''

    
    #print"........................................................................."
    #print "point 7"


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/can_tx", Frame, callback, queue_size=64)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    os.system('clear')
