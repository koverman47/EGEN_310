#!/usr/bin/env python3

import RPi.GPIO as gpio
import pigpio
import subprocess
import tty
import termios
import sys
import time

# in, in, en (PWM)
fore = [29, 31, 33]
aft = [16, 18, 12]
power = 50
max_pwm = 100

#servo_pin = 32
#servo = 25

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
#pwm_servo = gpio.PWM(servo_pin, max_pwm)
#pwm_servo.start(0)
#pwm_servo.ChangeDutyCycle(25)
pi = pigpio.pi()
servo_pin = 12
servo = 1500
pi.set_servo_pulsewidth(servo_pin, servo)
#subprocess.run(["sudo", "pigpiod"])


tty.setcbreak(sys.stdin)
try:
    while True:
        key = ord(sys.stdin.read(1))
        if key == 100:
            # go
            print(key)
            pwm_fore.ChangeDutyCycle(power)
            pwm_aft.ChangeDutyCycle(power)
        elif key == 120:
            # stop
            print(key)
            pwm_fore.ChangeDutyCycle(0)
            pwm_aft.ChangeDutyCycle(0)
        elif key == 115:
            # switch direction
            print(key)
            gpio.output(fore[0], not gpio.input(fore[0]))
            gpio.output(fore[1], not gpio.input(fore[1]))
            gpio.output(aft[0], not gpio.input(aft[0]))
            gpio.output(aft[1], not gpio.input(aft[1]))
        elif key == 114:
            print(key)
            if servo > 1050:
                servo -= 50
            print("New Duty Cycle: %s" % servo)
            #pwm_servo.ChangeFrequency(servo)
            #pwm_servo.ChangeDutyCycle(servo)
            pi.set_servo_pulsewidth(servo_pin, servo)
        elif key == 108:
            print(key)
            if servo < 1950:
            	servo += 50
            print("New Duty Cycle: %s" % servo)
            #pwm_servo.ChangeFrequency(servo)
            #pwm_servo.ChangeDutyCycle(servo)
            pi.set_servo_pulsewidth(servo_pin, servo)
        elif key == 110:
            servo = 1500
            pi.set_servo_pulsewidth(servo_pin, servo)
except KeyboardInterrupt:
    pass
finally:
    # Return stdin to ECHO
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    old[3] = old[3] | termios.ECHO
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    # End GPIO
    pwm_fore.stop()
    pwm_aft.stop()
    #pwm_servo.stop()
    gpio.cleanup()

