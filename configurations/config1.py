import math
import pygame
from configurations.configuration import Configuration


class Config1(Configuration):
    description = "Axis (Joystick) for directional control and z to go."

    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 1"

    '''
    ' Axis joystick used for direction and power
    ' z button (back of controller) used to allow drive
    '''
    def resolveReadings(self, axis0, axis1, events):
        ret = None
        for e in events:
            if e.type == pygame.JOYBUTTONDOWN and e.button == 7:
                print(axis0, axis1)
                self.power = 90 * math.sqrt(axis0**2 + axis1**2)
                self.for_rev = 1 if axis1 < 0 else 0
                ret = (self.for_rev, self.power, self.turn)
            elif e.type == pygame.JOYBUTTONUP and e.button == 7:
                self.power = 0
                ret = (self.for_rev, self.power, self.turn)
            elif e.type == pygame.JOYAXISMOTION and abs(e.value) > 0.01:
                if self.controller.get_button(7):
                    self.power = 90 * math.sqrt(axis0**2 + axis1**2)
                self.turn = (-160 * axis0) + 1500
                self.for_rev = 1 if axis1 < 0 else 0
                ret = (self.for_rev, self.power, self.turn)
        return ret

    def getConfigDescription(self):
        return description
