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
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
TSensor = TouchSensor(Port.S1)

# Setting the default speed.
speed = 100

while True: 
# Drive forward and accelerate each second, up to 5s.
    if TSensor.pressed():
        print("Touch sensor pressed!")  # Debugging.
        
        for i in range(1, 6): 
            # Increasing speed.
            speed += 100
    
            # Drive motors at current speed + acceleration
            left_motor.run(speed)
            right_motor.run(speed)
    
            # Wait for one second
            wait(1000)
    
        # Stop motors at the end
        left_motor.stop()
        right_motor.stop()