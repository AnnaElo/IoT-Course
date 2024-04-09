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

# Initialize.
TSensor = TouchSensor(Port.S1)

# Count how often the touch sensor has been pressed
# When the program starts, the robot shall count for 5 seconds, how often the touch sensor has been pressed. 
# This number shall be shown on the display.
# After the 5 seconds, the robot shall play a tone as many times as the touch sensor was pressed. 

# Code structure

button_count = 0
watch = StopWatch()

while watch.time() < 5000: 
    if TSensor.pressed():
        button_count += 1
        ev3.screen.clear()
        print("Count: {}" .format(button_count)) 
        ev3.screen.print("Count: {}" .format(button_count))
    wait(10) #10 milisecond wait

#for the sound part
for i in range(button_count):
    ev3.speaker.beep()