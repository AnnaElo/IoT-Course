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
left_motor.run_time(360, 2000, Stop.COAST, False)

right_motor = Motor(Port.C)
right_motor.run_time(360, 2000, Stop.COAST, False)

# Create your objects here.
ev3 = EV3Brick()

# Drive the figure „8“ 
from time import sleep

# Define the movements for the figure-8 pattern
# Adjust the durations and speeds as needed

movements = [
    (1, 50, 1),   # Move forward for 1 second at 50% speed
    (0.5, -50, 1),  # Turn left for 0.5 seconds at 50% speed
    (1, 50, 1),   # Move forward for 1 second at 50% speed
    (0.5, -50, 1),  # Turn left for 0.5 seconds at 50% speed
    (1, 50, 1),   # Move forward for 1 second at 50% speed
    (0.5, -50, 1),  # Turn left for 0.5 seconds at 50% speed
    (1, 50, 1),   # Move forward for 1 second at 50% speed
    (0.5, -50, 1)   # Turn left for 0.5 seconds at 50% speed
]

# Execute the movements
for move in movements:
    duration, speed_left, speed_right = move
    tank_drive.on_for_seconds(speed_left, speed_right, duration)
    sleep(0.1)  # Add a small delay between movements

# Stop the motors when done
tank_drive.off()