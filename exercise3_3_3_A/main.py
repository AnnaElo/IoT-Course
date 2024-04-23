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
MQTT_Topic_Command = 'Command'
MQTT_Topic_Ultrasonic = 'Ultrasonic' 
client = MQTTClient(MQTT_ClientID, MQTT_Broker, 1883)

# EV3 setup
ev3 = EV3Brick()
TSensor = TouchSensor(Port.S1)

# Write your program here.
def ultrasonicsensor_val(topic, msg):
    if topic == MQTT_Topic_Ultrasonic.encode():
        distance = str(msg.decode())
        ev3.screen.clear()
        ev3.screen.print("Distance: {}".format(distance))

client.set_callback(ultrasonicsensor_val)
client.connect()
client.subscribe(MQTT_Topic_Ultrasonic)


# Write your program here // Depending on which button is pressed, the robot shall play a different tone.
while True:
    pressed_buttons = ev3.buttons.pressed()
    ev3.screen.clear()

    if Button.UP in pressed_buttons:
        client.publish(MQTT_Topic_Command, 'FORWARD')
        ev3.screen.print('Up button pressed')
    elif Button.DOWN in pressed_buttons:
        client.publish(MQTT_Topic_Command, 'BACKWARD')
        ev3.screen.print('Down button pressed')
    elif Button.LEFT in pressed_buttons:
        client.publish(MQTT_Topic_Command, 'LEFT')
        ev3.screen.print('Left button pressed')
    elif Button.RIGHT in pressed_buttons:
        client.publish(MQTT_Topic_Command, 'RIGHT')
        ev3.screen.print('Right button pressed')
    elif Button.CENTER in pressed_buttons:
        client.publish(MQTT_Topic_Command, 'STOP')
        ev3.screen.print('Center button pressed')    

    client.check_msg()   
    time.sleep(0.1)