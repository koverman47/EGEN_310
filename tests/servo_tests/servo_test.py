#!/usr/bin/env python3

import RPi.GPIO as gpio
import tty
import termios
import sys
import time

servo_pin = 12
duty = 25
pwm = 90

# GPIO Setup
gpio.setmode(gpio.BOARD)
gpio.setup(servo_pin, gpio.OUT)

# pwm
pwm_servo = gpio.PWM(servo_pin, pwm)
pwm_servo.ChangeDutyCycle(duty)
pwm_servo.start(25)

for i in range(30):
    pwm += 1
    time.sleep(0.1)
    pwm_servo.ChangeFrequency(pwm)
pwm = 90
for j in range(30):
    pwm -= 1
    time.sleep(0.1)
    pwm_servo.ChangeFrequency(pwm)



tty.setcbreak(sys.stdin)
try:
    while True:
        key = ord(sys.stdin.read(1))
        if key == 114:
            print(key)
            if duty > 5:
                duty -= 5
            if pwm > 20:
                pwm -= 20
            print("New Duty Cycle: %s" % duty)
            print("New PWM: %s" % pwm)
            pwm_servo.ChangeFrequency(pwm)
            pwm_servo.ChangeDutyCycle(duty)
        elif key == 108:
            print(key)
            if duty < 95:
            	duty += 5
            if pwm < 235:
                pwm += 20
            print("New Duty Cycle: %s" % duty)
            print("New PWM: %s" % pwm)
            pwm_servo.ChangeFrequency(pwm)
            pwm_servo.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    pass
finally:
    # Return stdin to ECHO
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    old[3] = old[3] | termios.ECHO
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    # End GPIO
    pwm_servo.stop()
    gpio.cleanup()
    print("All clean!")

