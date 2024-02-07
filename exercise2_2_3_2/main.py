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

# Drive the figure „8“ 
from time import sleep

# Define the movements for the figure-8 pattern
# Adjust the durations and speeds as needed
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Function to drive in a figure "8"
def drive_figure_8(drive_speed, turn_rate, loop_duration):
    # Start the first loop of the "8" by turning in one direction
    robot.drive(drive_speed, turn_rate)
    time.sleep(loop_duration)
    # Reverse the turn rate for the second loop, creating the other half of the "8"
    robot.drive(drive_speed, -turn_rate)
    time.sleep(loop_duration)
    # Stop the robot after completing the figure "8"
    robot.stop()

# Example parameters (adjust based on your robot and desired size of the "8")
drive_speed = 120  # Speed in mm/s
turn_rate = 50  # Turn rate in degrees per second
loop_duration = 6  # Duration of each loop in seconds

# Drive in a figure "8"
drive_figure_8(drive_speed, turn_rate, loop_duration)
left_motor.stop()
right_motor.stop()