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

# Initial speed in mm/s
initial_speed = 100
# Speed increment in mm/s (how much to increase speed each second)
speed_increment = 50
# Current speed
current_speed = initial_speed

# Duration of acceleration in seconds
acceleration_duration = 10

# Start driving forward and accelerate each second
for _ in range(acceleration_duration):
    # Set the robot to drive at the current speed
    robot.drive(current_speed, 0)
    # Wait for 1 second
    time.sleep(1)
    # Increase the speed for the next iteration
    current_speed += speed_increment

# After finishing the acceleration, stop the robot
robot.stop()
