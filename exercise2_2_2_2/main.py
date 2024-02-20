#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initializing.
left_motor = Motor(Port.B)
left_motor.run_time(360, 2000, Stop.COAST, False)

# Create your objects here.
ev3 = EV3Brick()

# Drive in a circle
import time
left_motor.run(360)
time.sleep(8)
left_motor.stop()