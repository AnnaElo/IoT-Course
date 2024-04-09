#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# MQTT setup
MQTT_ClientID = 'Robot A'
MQTT_Broker = '192.168.0.39' # Change this to Eclipse Mosquitto ip address
MQTT_Topic_Status = 'Status'
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# EV3 setup
ev3 = EV3Brick()
ev3.speaker.beep()
sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)
watch = StopWatch()

def listen(topic, msg):
    message = msg.decode()
    if message == 'Robot A: Continue':
        ev3.screen.print('Continue')
        robot.drive(50, 0)  # Resume movement
        time.sleep(2)  # Move for a bit before stopping to listen again
        robot.stop()

client.connect()
client.set_callback(listen)
client.subscribe(MQTT_Topic_Status)

robot.drive(50, 0)  # Start driving

while True:
    distance = sensor.distance()
    if distance < 200:  # Adjust the distance as needed
        robot.stop()
        client.publish(MQTT_Topic_Status, 'Robot B: Move')
        ev3.screen.print('Waiting for Robot B')
        break
    wait(100)

client.check_msg()  # Check for messages from Robot B

