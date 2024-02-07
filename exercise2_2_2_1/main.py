#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = Motor(Port.B)
left_motor.run_time(30, 2000, Stop.COAST, False)

right_motor = Motor(Port.C)
right_motor.run_time(0, 2000, Stop.COAST, False)

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Drive straight 2 seconds.
import time
left_motor.run(360)
right_motor.run(360)
time.sleep(2)
left_motor.stop()
right_motor.stop()
