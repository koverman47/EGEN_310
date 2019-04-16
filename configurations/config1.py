import math
from configurations.configuration import Configuration


class Config1(Configuration):
    description = "Only Axis (Joystick) Control."

    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 1"

    def resolveReadings(self, axis0, axis1):
        for_rev = 1 if axis1 < 0 else 0
        power = 90 * math.sqrt(axis0**2 + axis1**2)
        turn = (450 * axis0) + 1500
    
        return (for_rev, power, turn)

    def getConfigDescription(self):
        return description
