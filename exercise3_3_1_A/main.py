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

# EV3 setup
ev3 = EV3Brick()

# MQTT setup
MQTT_ClientID = 'Robot_A'
MQTT_Broker = '192.168.0.39' # Change this to Eclipse Mosquitto ip address
MQTT_Topic_Status = 'Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# Callback for listen to topics
def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        message = str(msg.decode())
        ev3.screen.clear()
        ev3.screen.print(message)

# Program for robot A
client.connect()
time.sleep(0.5)
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)

while True:
    client.check_msg()
    time.sleep(0.5)