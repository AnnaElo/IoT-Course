#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


# Create your objects here.
ev3 = EV3Brick()

# Change of Direction and Speed.
robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)
robot.drive(600, 0) 
time.sleep(2)       
robot.drive(-300, 0) 
time.sleep(2)

