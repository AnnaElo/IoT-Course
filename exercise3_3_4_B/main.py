#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

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


def listen(topic, msg):
    message = msg.decode()
    if message == 'Robot B: Move':
        ev3.screen.print('Moving Away')
        robot.drive(-50, 0)  # Move backward or to the side to clear the path
        time.sleep(2)  # Move for a bit before stopping
        robot.stop()
        client.publish(MQTT_Topic_Status, 'Robot A: Continue')
        ev3.screen.print('Signaled Robot A to Continue')

client.connect()
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)

# Robot B doesn't move until it receives a message from Robot A
while True:
    client.check_msg()
    time.sleep(0.1)  # Check for messages periodically