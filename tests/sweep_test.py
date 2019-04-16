#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time


pin = 32
neutral = 1.5
frequency = 20

def getDuty(change):
    result = ((neutral + change) / frequency) * 100
    return result

def getHertz(length):
    result = 1. / float(length / 1000)
    return result

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, getHertz(frequency))
p.start(getDuty(0))

try:
    while True:
        p.ChangeDutyCycle(getDuty(0))
        time.sleep(0.1)
        p.ChangeDutyCycle(getDuty(-0.5))
        time.sleep(0.1)
        p.ChangeDutyCycle(getDuty(0))
        time.sleep(0.1)
        p.ChangeDutyCycle(getDuty(0.5))
        time.sleep(0.1)
except KeyboardInterrupt:
    p.stop
    GPIO.cleanup()
