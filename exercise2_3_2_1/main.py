#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()

# Initialize.
UltraSensor = UltrasonicSensor(Port.S2)

left_motor = Motor(Port.B)
left_motor.run_time(360, 2000, Stop.COAST, False)

right_motor = Motor(Port.C)
right_motor.run_time(360, 2000, Stop.COAST, False)

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# Write your program here.
robot.straight(400)

if UltraSensor.distance() > 200:
    wait(10)

    robot.stop()