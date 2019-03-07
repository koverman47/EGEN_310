#!/usr/bin/env python3

import RPi.GPIO as gpio
import tty
import termios
import sys
import time

# in, in, en (PWM)
fore = [29, 31, 33]
aft = [16, 18, 12]

# GPIO Setup
gpio.setmode(gpio.BOARD)
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
pwm_fore = gpio.PWM(fore[2], 100)
pwm_aft = gpio.PWM(aft[2], 100)
pwm_fore.start(0)
pwm_aft.start(0)


tty.setcbreak(sys.stdin)
try:
    while True:
        key = ord(sys.stdin.read(1))
        if key == 100:
            # go
            p.changeDutyCycle(50)
        elif key == 120:
            # stop
            p.changeDutyCycle(0)
        elif key == 115:
            # switch direction
            gpio.output(fore[0], not gpio.input(fore[0]))
            gpio.output(fore[1], not gpio.input(fore[1]))
            gpio.output(aft[0], not gpio.input(aft[0]))
            gpio.output(aft[1], not gpio.input(aft[1]))
except KeyboardInterrupt:
    pass

fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
old[3] = old[3] | termios.ECHO
termios.tcsetattr(fd, termios.TCSADRAIN, old)


pwm_fore.stop()
pwm_aft.stop()
gpio.cleanup()

