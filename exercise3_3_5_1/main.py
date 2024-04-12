#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from threading import Thread
import time

# EV3 setup
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)
ev3.speaker.beep()

from threading import Thread
import time


song = "C4,2,E4,4,G4,4,C4,2,E4,4,G4,4,A4,4,F4,4,A4,4,F4,4,C5,4"

notes = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "C5": 523.25,
}


class Robot(Thread):
    def __init__(self, note):
        super().__init__()
        self.note = note

    def run(self):
        global song
        while True:
            if self.note in song:
                print(f"Playing note: {self.note}")

               

                song = song.replace(f"{self.note},", "", 1)
                time.sleep(1) 


robots = [Robot(note) for note in notes.keys()]


num_robots = len(robots)
num_notes = len(notes)
for i in range(num_robots):
    robots[i].note = list(notes.keys())[i % num_notes]


for robot in robots:
    robot.start()


for robot in robots:
    robot.join()

print("Song finished!")


