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

# The robot should play a different sound depending on the color when recognizing different colors.

while True:
    # Get the color detected by the sensor.
    color = CSensor.color()
    
    # Compare the detected color with predefined color values.
    if color == Color.RED:
        ev3.speaker.beep(frequency=261.63, duration=500)  # C note
    elif color == Color.GREEN:
        ev3.speaker.beep(frequency=293.66, duration=500)  # D note
    elif color == Color.BLUE:
        ev3.speaker.beep(frequency=329.63, duration=500)  # E note
    elif color == Color.YELLOW:
        ev3.speaker.beep(frequency=349.23, duration=500)  # F note
    elif color == Color.WHITE:
        ev3.speaker.beep(frequency=392.00, duration=500)  # G note
    elif color == Color.BLACK:
        ev3.speaker.beep(frequency=440.00, duration=500)  # A note
    else:
        ev3.speaker.beep(frequency=0, duration=500)  # No beep if not detected color

    # Add a short delay to avoid excessive printing.
    wait(100)