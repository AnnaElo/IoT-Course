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

# Initialize motors. 
left_motor = Motor(Port.B)
left_motor.run_time(360, 2000, Stop.COAST, False)

right_motor = Motor(Port.C)
right_motor.run_time(360, 2000, Stop.COAST, False)

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
Turns = 4
Count = 0

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

while Turns > 0:
    robot.straight(400)
    robot.turn(90)
    Turns -= 1

    if Count == 4:
        left_motor.stop()
        right_motor.stop()