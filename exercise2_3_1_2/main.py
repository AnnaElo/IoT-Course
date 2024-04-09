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
TSensor = TouchSensor(Port.S1)

# Play a tone
# Each time when pressing the touch sensor, the robot shall play a tone.
# Hint: For this task, you have to combine a loop (while:) with a condition (if:).

# Loop structure for the code.
while True: 
    if TSensor.pressed():
        ev3.speaker.beep(frequency=261.63, duration=500)  # C note 