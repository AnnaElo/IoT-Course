#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from umqtt.robust import MQTTClient
import time

# MQTT setup
MQTT_ClientID = 'Robot A'
MQTT_Broker = '192.168.0.39' # Change this to Eclipse Mosquitto ip address
MQTT_Topic_Status = 'Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)
client.connect()

# EV3 setup
ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)
watch = StopWatch()

def mqtt_callback(topic, msg):
    if topic == MQTT_Topic_Status:
        message = str(msg.decode())
        if message == 'Continue':
            ev3.screen.print('Message received')
            robot.drive(50, 0)  # Resume movement
            time.sleep(2)  # Move for a bit before stopping to listen again
            robot.stop()

client.set_callback(mqtt_callback)
client.subscribe(MQTT_Topic_Status)

robot.drive(50, 0)  # Start driving

while True:
    distance = sensor.distance()
    if distance < 200:  # Adjust the distance as needed
        robot.stop()
        client.publish(MQTT_Topic_Status, 'Robot B: Move')
        ev3.screen.print('Waiting for Robot B')
    time.sleep(0.5)