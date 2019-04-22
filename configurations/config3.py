import math
import pygame
from configurations.configuration import Configuration

class Config3(Configuration):
    description = "Axis (Joystick) for turn and power. A/B for forward/reverse."

    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 3"
        self.a = False
        self.b = False

    '''
    ' Axis joystick controls power and turn
    ' A allows forward drive
    ' B allows reverse drive
    '''
    def resolveReadings(self, axis0, axis1, events):
        ret = None
        change = False
        for e in events:
            if e.type == pygame.JOYBUTTONDOWN:
                if e.button == 6:
                    self.for_rev = 1
                    self.a = True
                    change = True
                elif e.button == 8:
                    self.for_rev = 0
                    self.b = True
                    change = True
                ret = (self.for_rev, self.power, self.turn)
            elif e.type == pygame.JOYBUTTONUP:
                if e.button == 6:
                    self.a = False
                    change = True
                elif e.button == 8:
                    self.b = False
                    change = True
            elif e.type == pygame.JOYAXISMOTION:
                self.power = 90 * math.sqrt(axis0**2 + axis1**2)
                self.turn = (-160 * axis0) + 1500
                ret = (self.for_rev, self.power, self.turn)
                change = True

        if (not self.a and not self.b) or (self.a and self.b):
            self.power = 0
            ret = (self.for_rev, self.power, self.turn)
        if not change:
            return None
        return ret

    def getConfigDescription(self):
        return description 
