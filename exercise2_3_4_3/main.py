#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from umqtt.simple import MQTTClient


MQTT_BROKER = "your_broker_ip"
MQTT_TOPIC = "robot_commands"


def play_tone(button):
    if button == Button.UP:
        ev3.speaker.beep(1000, 500)
    elif button == Button.DOWN:
        ev3.speaker.beep(1500, 500)
    elif button == Button.LEFT:
        ev3.speaker.beep(2000, 500)
    elif button == Button.RIGHT:
        ev3.speaker.beep(2500, 500)
    elif button == Button.CENTER:
        ev3.speaker.beep(3000, 500)


def mqtt_callback(topic, msg):
    button = Button[msg.decode()]
    play_tone(button)


client = MQTTClient("ev3", MQTT_BROKER)
client.set_callback(mqtt_callback)
client.connect()


client.subscribe(MQTT_TOPIC)


ev3 = EV3Brick()


while True:
    client.check_msg()  
    pressed_buttons = ev3.buttons.pressed()
    ev3.screen.clear()

    if Button.UP in pressed_buttons:
        ev3.screen.print("Up button pressed")
        client.publish(MQTT_TOPIC, "UP")
    elif Button.DOWN in pressed_buttons:
        ev3.screen.print("Down button pressed")
        client.publish(MQTT_TOPIC, "DOWN")
    elif Button.LEFT in pressed_buttons:
        ev3.screen.print("Left button pressed")
        client.publish(MQTT_TOPIC, "LEFT")
    elif Button.RIGHT in pressed_buttons:
        ev3.screen.print("Right button pressed")
        client.publish(MQTT_TOPIC, "RIGHT")
    elif Button.CENTER in pressed_buttons:
        ev3.screen.print("Center button pressed")
        client.publish(MQTT_TOPIC, "CENTER")
        
    wait(100)
