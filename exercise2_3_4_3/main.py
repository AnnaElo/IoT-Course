#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

# Write your program here // Only one button pressed at the time
# Write your program here // Depending on which button is pressed, the robot shall play a different tone.

while True:
    pressed_buttons = ev3.buttons.pressed()
    ev3.screen.clear()

    if Button.UP in pressed_buttons:
        ev3.screen.print("Up button pressed")
        ev3.speaker.beep(frequency=261.63, duration=500)  # C note
    elif Button.DOWN in pressed_buttons:
        ev3.screen.print("Down button pressed")
        ev3.speaker.beep(frequency=293.66, duration=500)  # D note
    elif Button.LEFT in pressed_buttons:
        ev3.screen.print("Left button pressed")
        ev3.speaker.beep(frequency=329.63, duration=500)  # E note
    elif Button.RIGHT in pressed_buttons:
        ev3.screen.print("Right button pressed")
        ev3.speaker.beep(frequency=349.23, duration=500)  # F note
    elif Button.CENTER in pressed_buttons:
        ev3.screen.print("Center button pressed")                      
        ev3.speaker.beep(frequency=392.00, duration=500)  # G note             
    wait(100)