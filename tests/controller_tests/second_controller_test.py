#!/usr/bin/env python3

import pygame
import sys
import time


pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

i = 0
print(j.get_numaxes())
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                print("print button pressed")
                print(event.value)
            elif event.type == pygame.JOYHATMOTION:
                print("Hat motion", event.value)
            elif event.type == pygame.JOYAXISMOTION and abs(event.value) > 0.1:
                print(event.axis, event.value)
                i += 1
        if j.get_button(9):
            raise KeyboardInterrupt
        time.sleep(0.5)
except KeyboardInterrupt:
    j.quit()
    sys.exit(0)
