#!/usr/bin/env python3

import pigpio
from time import sleep

# Run the following command first
# sudo pigpiod

pi = pigpio.pi()
pin = 12

while True:
    pi.set_servo_pulsewidth(12, 0)
    sleep(1)
    pi.set_servo_pulsewidth(12, 1000)
    sleep(1)
    pi.set_servo_pulsewidth(12, 1500)
    sleep(1)
    pi.set_servo_pulsewidth(12, 2000)
    sleep(1)
