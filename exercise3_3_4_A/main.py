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

#Robot A
while True:
    distance = sensor_a.distance()

    if distance < 200:  # Robot A close enough (adjustable threshold)
        is_robot_a_in_front = True
        left_motor.stop()
        right_motor.stop() 
        break  

     left_motor.run(360)
     right_motor.run(360)
      

    

