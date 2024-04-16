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
        elif color == Color.BLUE:
            ev3.speaker.beep(frequency=293.66, duration=500)  # D note
        elif color == Color.BLACK:
            ev3.speaker.beep(frequency=440.00, duration=500)  # A note
        elif color == Color.YELLOW:
            ev3.speaker.beep(frequency=349.23, duration=500)  # F note

# Count the lines and detect the colors
colors_count = {Color.RED: 0, Color.BLUE: 0, Color.BLACK: 0, Color.YELLOW: 0}

# Mapping between color values and their names
COLOR_NAMES = {
    Color.RED: "RED",
    Color.BLUE: "BLUE",
    Color.BLACK: "BLACK",
    Color.YELLOW: "YELLOW"
}

watch = StopWatch()

start_time = watch.time()
while watch.time() - start_time < 10000:
    robot.drive(100, 0)

    color = CSensor.color()

    if color in colors_count:
        colors_count[color] += 1
        ev3.screen.clear()
        color_name = COLOR_NAMES.get(color, "")
        ev3.screen.print("{} lines count: {}".format(color_name, colors_count[color]))  # Display detected color
        print("{} lines count: {}".format(color_name, colors_count[color]))
        
    wait(10)  # 10 millisecond wait

robot.stop()  # Stop the robot after 10 seconds

# Modify the second while loop for button handling
button_pressed = False
button_released = False

while True:
    if Button.CENTER in ev3.buttons.pressed() and not button_pressed:
        button_pressed = True
        color_sequence.append(CSensor.color())
        ev3.screen.clear()
        ev3.screen.print("Sequence: " + ', '.join(COLOR_NAMES[c] for c in color_sequence))
    elif Button.CENTER not in ev3.buttons.pressed() and button_pressed:
        button_pressed = False
        play_tones()
        color_sequence.clear()
        ev3.screen.clear()
        ev3.screen.print("Sequence cleared")
    
    wait(10)  # 10 millisecond wait