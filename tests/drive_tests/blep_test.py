#!/usr/bin/env python3

import RPi.GPIO as gpio
import pigpio
import pygame
import subprocess
import tty
import termios
import sys
import time

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

# in, in, en (PWM)
fore = [29, 31, 33]
aft = [16, 18, 12]
max_pwm = 100

# GPIO Setup
gpio.setmode(gpio.BOARD)
#gpio.setup(servo_pin, gpio.OUT)
for i in range(3):
    gpio.setup(fore[i], gpio.OUT)
    gpio.setup(aft[i], gpio.OUT)

# in1, in2
gpio.output(fore[0], gpio.LOW)
gpio.output(fore[1], gpio.HIGH)

# in3, in4
gpio.output(aft[0], gpio.LOW)
gpio.output(aft[1], gpio.HIGH)

# pwm
pwm_fore = gpio.PWM(fore[2], max_pwm)
pwm_aft = gpio.PWM(aft[2], max_pwm)
pwm_fore.start(0)
pwm_aft.start(0)

pi = pigpio.pi()
servo_pin = 12
servo = 1500
pi.set_servo_pulsewidth(servo_pin, servo)


forward = True
try:
    while True:
        if not j.get_button(7):
            pwm_fore.ChangeDutyCycle(0)
            pwm_aft.ChangeDutyCycle(0)
        else:
            power = j.get_axis(1)
            if power > 0 and forward:
                forward = False
                gpio.output(fore[0], not gpio.input(fore[0]))
                gpio.output(fore[1], not gpio.input(fore[1]))
                gpio.output(aft[0], not gpio.input(aft[0]))
                gpio.output(aft[1], not gpio.input(aft[1]))
            elif power < 0 and not forward:
                forward = True
                gpio.output(fore[0], not gpio.input(fore[0]))
                gpio.output(fore[1], not gpio.input(fore[1]))
                gpio.output(aft[0], not gpio.input(aft[0]))
                gpio.output(aft[1], not gpio.input(aft[1]))
            pwm_fore.ChangeDutyCycle(abs(power) * 90)
            pwm_aft.ChangeDutyCycle(abs(power) * 90)
        pi.set_servo_pulsewidth(servo_pin, j.get_axis(0) * 490 + servo)


except KeyboardInterrupt:
    pass
finally:
    j.quit()
    # End GPIO
    pwm_fore.stop()
    pwm_aft.stop()
    gpio.cleanup()

