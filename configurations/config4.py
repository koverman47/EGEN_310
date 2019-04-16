import math
from configurations.configuration import Configuration

class Config4(Configuration):
    description = "Axis (Joysick) + Z for forward and R for reverse."

    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 4"

    def resolveReadings(self, axis0, axis1):
        z = self.controller.get_button(7)
        r = self.controller.get_button(5)

        if (not z and not r) or (z and r):
            return (1, 0, 1500)

        power = 90 * math.sqrt(axis0**2 + axis1**2)
        turn = (450 * axis0) + 1500

        return (z, power, turn)

    def getConfigDescription(self):
        return description 
