#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# EV3 setup
ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=104)
ev3.speaker.beep()

# Write your program here.
from threading import Thread
import random
import time

# Define room dimensions (adjust as needed)
room_width = 5
room_height = 5

# Define sensor range for wall detection
sensor_range = 0.5  # Units (e.g., meters)

# Define message for central maintenance manager
inspection_message = "Robot {id} needs inspection!"

# Simulated communication with central maintenance manager (replace with actual communication method)
def send_message(message):
    print(f"Sending message: {message}")

# Simulated warning signal (replace with actual sound or visual signal)
def emit_warning(robot_id):
    print(f"Warning! Robot {robot_id} needs inspection.")

class Robot(Thread):
    def __init__(self, robot_id, led_control, message_sender):
        super().__init__()
        self.id = robot_id
        self.x = random.uniform(0, room_width)  # Initial random position (X)
        self.y = random.uniform(0, room_height)  # Initial random position (Y)
        self.direction = random.choice(["up", "down", "left", "right"])  # Initial random direction
        self.wall_count = 0
        self.led_control = led_control
        self.message_sender = message_sender

    def run(self):
        while self.wall_count < 10:
            # Check for wall collision
            if self.check_collision():
                self.wall_count += 1
                self.change_direction()

                # Turn LED red on wall collision
                self.led_control.set_color(self.id, "red")

                # Send message for inspection
                self.message_sender(inspection_message.format(id=self.id))
                emit_warning(self.id)
                time.sleep(2)  # Simulate pause after hitting a wall

            # Update position based on direction
            self.move()

            # Simulate random movement time
            time.sleep(random.uniform(0.5, 1))  # Adjust movement time as needed

        # Stop robot after reaching wall limit
        self.led_control.set_color(self.id, "red")  # Keep LED red
        print(f"Robot {self.id} stopped after reaching 10 walls.")

    def check_collision(self):
        # Check for wall collision based on direction and sensor range
        if self.direction == "up" and self.y + sensor_range >= room_height:
            return True
        elif self.direction == "down" and self.y - sensor_range <= 0:
            return True
        elif self.direction == "left" and self.x - sensor_range <= 0:
            return True
        elif self.direction == "right" and self.x + sensor_range >= room_width:
            return True
        else:
            return False

    def change_direction(self):
        # Choose a new random direction when hitting a wall
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        # Update robot position based on direction
        if self.direction == "up":
            self.y += 0.1  # Adjust movement distance as needed
        elif self.direction == "down":
            self.y -= 0.1
        elif self.direction == "left":
            self.x -= 0.1
        elif self.direction == "right":
            self.x += 0.1

# Simulated LED control (replace with actual LED control method)
class LEDControl:
    def __init__(self):
        self.colors = {}

    def set_color(self, robot_id, color):
        self.colors[robot_id] = color
        print(f"Robot {robot_id} LED: {color}")  # Simulate setting LED color

# Main program
num_robots = 1  # Adjust the number of robots

# Create robots and LED control object
robots = []
led_control = LEDControl()
message_sender = send_hii  # type: ignore # Replace with actual message sending method

for i in range(num_robots):
    robots.append(Robot(i + 1, led_control, message_sender))

# Start robot threads
for robot in robots:
    robot.start()

