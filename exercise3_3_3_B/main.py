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
MQTT_Topic_Command = 'Command'
MQTT_Topic_Ultrasonic = 'Ultrasonic'  # Topic for sending ultrasonic sensor value to Robot A
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# EV3 setup
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S4)  # Ensure the correct port is used

# Callback function to handle command messages
def command_callback(topic, msg):
    if topic == MQTT_Topic_Command.encode():
        command = str(msg.decode())
        execute_command(command)

# Function to execute movements based on commands
def execute_command(command):
    if command == 'FORWARD':
        left_motor.run(360)
        right_motor.run(360)
    elif command == 'BACKWARD':
        left_motor.run(-360)
        right_motor.run(-360)
    elif command == 'LEFT':
        left_motor.run_time(-360, 1000)
        right_motor.run_time(360, 1000)
    elif command == 'RIGHT':
        left_motor.run_time(360, 1000)
        right_motor.run_time(-360, 1000)
    elif command == 'STOP':
        left_motor.stop()
        right_motor.stop()


client.set_callback(command_callback)
# client.connect()
client.subscribe(MQTT_Topic_Command)

# Main loop for publishing ultrasonic sensor values
while True:
    distance = ultrasonic_sensor.distance()
    client.publish(MQTT_Topic_Ultrasonic, str(distance))
    client.check_msg()  # Check for command messages
