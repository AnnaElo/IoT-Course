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
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
while True:

    # Get the distance measurement
    distance = ultrasonic_sensor.distance()
    
    # Depending on the distance, play different tones
    if distance < 100:
        ev3.speaker.beep(frequency=1000, duration=500)  # High pitch beep
    elif distance < 200:
        ev3.speaker.beep(frequency=500, duration=500)  # Medium pitch beep
    else:
        ev3.speaker.beep(frequency=250, duration=500)  # Low pitch beep
        
    wait(100)   