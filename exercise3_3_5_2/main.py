#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import random
import time

# EV3 setup
ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)


room_width = 5
room_height = 5


sensor_range = 0.5  


inspection_message = "Robot {id} needs inspection!"


def send_message(message):
    print("Sending message: {}".format(message))


class LEDControl:
    def __init__(self):
        self.colors = {}

    def set_color(self, robot_id, color):
        self.colors[robot_id] = color
        print("Robot {} LED: {}".format(robot_id, color))


def emit_warning(robot_id):
    print("Warning! Robot {} needs inspection.".format(robot_id))

class Robot:
    def __init__(self, robot_id, led_control, message_sender):
        self.id = robot_id
        self.x = random.uniform(0, room_width)  
        self.y = random.uniform(0, room_height)  
        self.direction = random.choice(["up", "down", "left", "right"])  
        self.wall_count = 0
        self.led_control = led_control
        self.message_sender = message_sender

        # Initialize the drive base for the robot
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)

    def change_direction(self):
        # Turn the robot 90 degrees
        self.drive_base.turn(90)

    def run(self):
        while self.wall_count < 10:
           
            collision = random.choice([True, False])
            if collision:
                self.wall_count += 1
                self.change_direction()
                self.led_control.set_color(self.id, "red")
                self.message_sender(inspection_message.format(id=self.id))
                emit_warning(self.id)
                time.sleep(2)  

          
            self.move()
            time.sleep(random.uniform(0.5, 1))  

            if self.wall_count >= 10:
                self.led_control.set_color(self.id, "red")
                print("Robot {} stopped after reaching 10 walls.".format(self.id))
                break  

    


num_robots = 1  


led_control = LEDControl()

robots = [Robot(i + 1, led_control, send_message) for i in range(num_robots)]


for robot in robots:
    robot.run()  