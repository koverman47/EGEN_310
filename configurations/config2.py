import math
from configurations.configuration import Configuration


class Config2(Configuration):
    description = "Axis (Joystick) for directional control and Z to go."
    
    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 2"

    def resolveReadings(self, axis0, axis1):
        z = self.controller.get_button(7)
        for_rev = 1 if axis1 < 0 else 0
        if z:
            power = 90 * math.sqrt(axis0**2 + axis1**2)
        else:
            power = 0
        turn = (450 * axis0) + 1500

        return (for_rev, power, turn)

    def getConfigDescription(self):
        return description 
