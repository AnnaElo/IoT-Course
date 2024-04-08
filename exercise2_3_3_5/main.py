#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here
ev3 = EV3Brick()

# Initialize
CSensor = ColorSensor(Port.S3)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# Array to store the colors
color_sequence = []

# Play different notes to different colors
def play_tones():
    for color in color_sequence:
        if color == Color.RED:
            ev3.speaker.beep(frequency=261.63, duration=500)  # C note
        elif color == Color.GREEN:
            ev3.speaker.beep(frequency=293.66, duration=500)  # D note
        elif color == Color.BLACK:
            ev3.speaker.beep(frequency=440.00, duration=500)  # A note
        elif color == Color.YELLOW:
            ev3.speaker.beep(frequency=349.23, duration=500)  # F note

# Count the lines and detect the colors
colors_count = {Color.RED: 0, Color.GREEN: 0, Color.BLACK: 0, Color.YELLOW: 0}

watch = StopWatch()
color = CSensor.color()

# The robot shall drive forward and count how often it crosses a colored line
while watch.time() < 5000:
    robot.drive(50,0)

    if color in colors_count:
        colors_count[color] += 1
        ev3.screen.clear()
        print("{} lines count: {}".format(color.name(), colors_count[color]))
    
    wait(10)  # 10 millisecond wait

# Storing the detected colors
while True:
    if robot.buttons.pressed():
        color_sequence.append(CSensor.color())
        ev3.screen.clear()
        ev3.screen.print("Sequence: " + ', '.join(c.name() for c in color_sequence))
        wait(200)  # Wait for button release

    elif robot.buttons.released():
        play_tones()
        color_sequence.clear()
        ev3.screen.clear()
        ev3.screen.print("Sequence cleared")
        wait(200)  # Debounce button
        
    wait(10)  # 10 millisecond wait