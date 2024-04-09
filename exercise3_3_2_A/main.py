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
MQTT_ClientID = 'Robot A'
MQTT_Broker = '192.168.0.39' # Change this to Eclipse Mosquitto ip address
MQTT_Topic_Status = 'Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# EV3 setup
ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)
watch = StopWatch()

# Callback for listen to topics
def listen(topic,msg):
    if topic == MQTT_Topic_Status.encode():
        ev3.screen.print(str(msg.decode()))

# Write your program here
robot.drive(50, 0)

client.connect()
time.sleep(0.5)
client.publish(MQTT_Topic_Status, 'Started')
ev3.screen.print('Started')
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)
time.sleep(0.5)
client.publish(MQTT_Topic_Status, 'Listening')
ev3.screen.print('Listening')

# Loop until Robot B is detected nearby
while True:
    client.check_msg()
    distance = sensor.distance()
    if distance < 100:  
        client.publish(MQTT_Topic_Status, 'Close to Robot B')
        ev3.screen.print('Close to Robot B')
        break
    wait(100)  # Adjust wait time as needed

# Stop moving Robot A
robot.stop()

# Send message to Robot B to start driving
client.publish(MQTT_Topic_Status, 'Start Driving')
ev3.screen.print('Start Driving')