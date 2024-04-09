#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the ultrasonic sensor
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Create EV3 brick object
ev3 = EV3Brick()

while True:
    # Get the distance measurement
    distance = ultrasonic_sensor.distance()

    # Clear the display and show the distance
    ev3.screen.clear()
    ev3.screen.print("Distance: {} mm".format(distance))

    # Wait a short time before the next measurement
    wait(100) 
