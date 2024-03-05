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
CSensor = ColorSensor(Port.S3)
ev3.screen.print(CSensor.color())

# The color detected by the sensor shall be shown on the display.
while True:
    # Get the color detected by the sensor.
    color = CSensor.color()
    
    # Compare the detected color with predefined color values.
    if color == Color.RED:
        print("Red detected!")
    elif color == Color.GREEN:
        print("Green detected!")
    elif color == Color.BLUE:
        print("Blue detected!")
    elif color == Color.YELLOW:
        print("Yellow detected!")
    elif color == Color.WHITE:
        print("White detected!")
    elif color == Color.BLACK:
        print("Black detected!")
    else:
        print("Unknown color detected!")

    # Add a short delay to avoid excessive printing.
    wait(100)