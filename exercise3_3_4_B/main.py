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
MQTT_ClientID = 'Robot B'
MQTT_Broker = '192.168.0.39' # Change this to Eclipse Mosquitto ip address
MQTT_Topic_Status = 'Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# EV3 setup
ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)

def go_backward(distance_mm):
    # Time = Distance / Speed
    time_ms = int((distance_mm / 10) / 100 * 1000)  # Convert to milliseconds
    robot.drive_time(-100, 0, time_ms)  # Drive backward for the calculated time

#Robot B Listening
def listen(topic, msg):
    if topic == MQTT_Topic_Status.encode():
        message = str(msg.decode())

        if message == 'Robot B: Move':
            ev3.screen.print('Moving Away')
            go_backward(200)  # Distance in millimeters
            time.sleep(2) 
            robot.stop()
            client.publish(MQTT_Topic_Status, 'Continue')
            ev3.screen.print('Signaled Robot A to Continue')

# Listening 
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)

# Define the distance 
distance_between = 200  # 20cm converted to millimeters

def is_obstacle_nearby():
    return sensor.distance() < distance_between

# Robot B driving loop
while True:
    if not is_obstacle_nearby():
        robot.drive(100, 0)  # Move forward
    else:
        robot.stop()  # Stop if an obstacle is detected
    time.sleep(0.1) 