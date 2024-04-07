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

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=105)

# Count the lines and detect the colors.
RED_line_count = 0
GREEN_line_count = 0
BLACK_line_count = 0
YELLOW_line_count = 0

watch=StopWatch()
color = CSensor.color()

# The robot shall drive forward and count how often it crosses a colored line.
while watch.time() < 5000:
    robot.drive(50,0)

    if color == Color.RED:
        RED_line_count += 1
        ev3.screen.clear()
        print("Red lines count: {}" .format(RED_line_count)) #cal also be ev3.screen.print()
    wait(10) #10 milisecond wait

    if color == Color.GREEN:
        GREEN_line_count += 1
        ev3.screen.clear()
        print("Green lines count: {}" .format(GREEN_line_count)) #cal also be ev3.screen.print()
    wait(10) #10 milisecond wait    

    if color == Color.BLACK:
        BLACK_line_count += 1
        ev3.screen.clear()
        print("Black lines count: {}" .format(BLACK_line_count)) #cal also be ev3.screen.print()
    wait(10) #10 milisecond wait 

    if color == Color.YELLOW:
        YELLOW_line_count += 1
        ev3.screen.clear()
        print("Yellow lines count: {}" .format(YELLOW_line_count)) #cal also be ev3.screen.print()
    wait(10) #10 milisecond wait 


#for the sound part
#for i in range(line_count):
    #ev3.speaker.beep()
