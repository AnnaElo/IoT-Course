#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S4)


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
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

while True:
    # Get the distance measurement
    distance = ultrasonic_sensor.distance()
    
    # Clear the screen
    ev3.screen.clear()
    
    # Display the distance on the screen
    ev3.screen.print(f"Distance: {distance} mm")
    
    # Wait a bit before the next measurement to make the display readable
    wait(500)
