#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Import library
from umqtt.robust import MQTTClient
import time

# MQTT setup
MQTT_ClientID = 'Robot B'
MQTT_Broker = '192.168.0.39' # Change this to Eclipse Mosquitto ip address
MQTT_Topic_Status = 'Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# EV3 setup
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)

# Callback for listen to topics
def listen(topic, msg):
    if topic == MQTT_Topic_Status.encode() and msg.decode() == 'Close':
        ev3.screen.print('Close to Robot A')
        robot.drive_time(100, 0, 10000)  # Drive forward at 100 mm/s for 10 seconds (10000 milliseconds)
        time.sleep(10)
        robot.stop()


# Initializing MQTT
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)
ev3.screen.print('Listening')