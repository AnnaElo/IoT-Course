#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from threading import Thread
import time

# EV3 setup
ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)
ev3.speaker.beep()

from threading import Thread
import time

# Define the song as a string
song = "C4,2,E4,4,G4,4,C4,2,E4,4,G4,4,A4,4,F4,4,A4,4,F4,4,C5,4"

# Define the notes dictionary
notes = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "C5": 523.25,
}

# Define the robot class
class Robot(Thread):
    def __init__(self, note):
        super().__init__()
        self.note = note

    def run(self):
        global song
        while True:
            if self.note in song:
                print(f"Playing note: {self.note}")

                # Replace this with your actual LED control code
                # For example, if using a library:
                # from your_led_library import blink_led
                # blink_led(color="red")  # Adjust color as needed

                song = song.replace(f"{self.note},", "", 1)
                time.sleep(1)  # Simulate playing the note

# Create robots (assuming you have 7 robots)
robots = [Robot(note) for note in notes.keys()]

# Assign robots to notes (assuming an even distribution)
num_robots = len(robots)
num_notes = len(notes)
for i in range(num_robots):
    robots[i].note = list(notes.keys())[i % num_notes]

# Start the robots
for robot in robots:
    robot.start()

# Wait for all robots to finish
for robot in robots:
    robot.join()

print("Song finished!")

