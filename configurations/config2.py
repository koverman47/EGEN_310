import math
import pygame
from configurations.configuration import Configuration


class Config2(Configuration):
    description = "Only Axis (Joystick) Control."
    
    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 2"

    def resolveReadings(self, axis0, axis1, events):
        ret = None
        for e in events:
            if e.type == pygame.JOYAXISMOTION:
                self.for_rev = 1 if axis1 < 0 else 0
                self.turn = (-160 * axis0) + 1500
                self.power = 90 * math.sqrt(axis0**2 + axis1**2)
                ret = (self.for_rev, self.power, self.turn)
        return ret

    def getConfigDescription(self):
        return description 
