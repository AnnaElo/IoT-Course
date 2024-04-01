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


# Create your objects here.
ev3 = EV3Brick()
touch_sensor = TouchSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

def drive_straight():
    robot.drive(200,0)

def stop_robot():
    robot.stop()

def robot_turn():
    robot.turn(180)


# Write your program here.
while not touch_sensor.pressed():
    drive_straight()
    while ultrasonic_sensor.distance() > 200:
        wait(10)
    stop_robot()
    robot_turn()
