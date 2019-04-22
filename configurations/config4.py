import math
import pygame
from configurations.configuration import Configuration

class Config4(Configuration):
    description = "Axis (Joysick) + Z for forward and R for reverse."

    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 4"
        self.z = False
        self.r = False

    def resolveReadings(self, axis0, axis1, events):
        ret = None
        change = False
        for e in events:
            if e.type == pygame.JOYBUTTONDOWN:
                if e.button == 7:
                    self.z = True
                    self.for_rev = 1
                    change = True
                elif e.button == 5:
                    self.r = True
                    self.for_rev = 0
                    change = True
                ret = (self.for_rev, self.power, self.turn)
            elif e.type == pygame.JOYBUTTONUP:
                if e.button == 7:
                    self.z = False
                    change = True
                elif e.button == 5:
                    self.r = False
                    change = True
            elif e.type == pygame.JOYAXISMOTION:
                self.power = 90 * math.sqrt(axis0**2 + axis1**2)
                self.turn = (-160 * axis0) + 1500
                ret = (self.for_rev, self.power, self.turn)
                change = True
                
        if (not self.z and not self.r) or (self.z and self.r):
            self.power = 0
            ret = (self.for_rev, self.power, self.turn)
        if not change:
            return None
        #if change:
        #    print(ret)
        return ret

    def getConfigDescription(self):
        return description 
