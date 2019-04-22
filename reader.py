#!/usr/bin/env python3

import sys
import RPi.GPIO as gpio
import pigpio
import traceback

'''
' Establish Pinouts
' fore/aft: [in#, in#, pwm]
' servo: pwm
'''
fore = [29, 31, 33] # board pins
aft = [16, 18, 12] # board pins
servo = 12 # BCM pin (board 32)

# cap pwm for motors
max_pwm = 200

'''
' Setup GPIO for motors
'''
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

pwm_fore = gpio.PWM(fore[2], max_pwm)
pwm_aft = gpio.PWM(aft[2], max_pwm)

pwm_fore.start(0)
pwm_aft.start(0)

'''
' Setup servo gpio
'''
pi = pigpio.pi()
pi.set_servo_pulsewidth(servo, 1500)

'''
' Create Log file
'''
f = open("out.log", "w+")
forward = True
try:
    while True:
        '''
        ' Read from stdin
        '''
        var = input()
        if var == "exit":
            break
        '''
        ' Parse and log data
        '''
        data = var.rstrip().split("|")
        f.write(data[0] + " " + data[1] + " " + data[2] + "\n")
        data[0] = int(data[0])
        data[1] = int(data[1])
        data[2] = int(data[2])

        '''
        ' Change direction of motors
        '''
        if (data[0] == 0 and forward) or (data[0] == 1 and not forward):
            forward = not forward
            gpio.output(fore[0], not gpio.input(fore[0]))
            gpio.output(fore[1], not gpio.input(fore[1]))
            gpio.output(aft[0], not gpio.input(aft[0]))
            gpio.output(aft[1], not gpio.input(aft[1]))

        '''
        ' Cap motor duty cycle
        ' 0 <= dc <= 100
        '''
        if data[0] < 0:
            data[0] = 0
        elif data[0] > 100:
            data[0] = 100
        if data[1] < 0:
            data[1] = 0
        elif data[1] > 100:
            data[1] = 100

        '''
        ' Set new motor duty cycle
        ' set servo pwm
        '''
        pwm_fore.ChangeDutyCycle(data[1])
        pwm_aft.ChangeDutyCycle(data[1])
        pi.set_servo_pulsewidth(servo, data[2])
except EOFError as e:
    f.write(e)
except:
    f.write(traceback.format_exc() + "\n")
finally:
    '''
    ' Log out close
    ' close log file
    '''
    f.write("Done")
    f.close()

    '''
    ' Stop motors
    ' Clean GPIO
    '''
    pwm_fore.stop()
    pwm_aft.stop()
    gpio.cleanup()
