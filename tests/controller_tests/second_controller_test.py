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
            if event.type == pygame.JOYBALLMOTION:
                print("Ball Motion")
           # elif event.type == pygame.JOYBUTTONDOWN:
           #     print("print button pressed")
           #     for b in range(12):
           #         print(b, j.get_button(b))
           # elif event.type == pygame.JOYHATMOTION:
           #     print("Hat motion", event.value)
           # elif event.type == pygame.JOYAXISMOTION and abs(event.value) > 0.1:
           #     print(event.axis, event.value)
           #     i += 1
            pass
        print(j.get_axis(0), j.get_axis(1), j.get_axis(2))
        time.sleep(1)
except KeyboardInterrupt:
    j.quit()
    sys.exit(0)