#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Color
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

# Function to play a note
def play_note(note, duration):
    if note in notes:
        frequency = notes[note]
        ev3.speaker.beep(frequency=frequency, duration=duration * 100)  # Duration is in milliseconds

# Function to play the song
def play_song(song):
    notes_in_song = song.split(',')
    for i in range(0, len(notes_in_song), 2):
        note = notes_in_song[i]
        duration = int(notes_in_song[i + 1])
        play_note(note, duration)
        time.sleep(duration / 10)  # Adjust sleep to match the rhythm of the song

play_song(song)

print("Song finished!")


