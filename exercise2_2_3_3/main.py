#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# Initialize
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Create your objects here.
ev3 = EV3Brick()

# Change of Direction and Speed.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

robot.settings(straight_speed=1000)


robot.straight(1000) 
time.sleep(2)       
ev3.speaker.beep()
robot.straight(-1000)  
robot.stop()