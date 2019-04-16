import math
from configurations.configuration import Configuration

class Config3(Configuration):
    description = "Axis (Joystick) for turn and power. A/B for forward/reverse."

    def __init__(self, controller):
        Configuration.__init__(self, controller)
        self.name = "Configuration 3"

    def resolveReadings(self, axis0, axis1):
        a = self.controller.get_button(6)
        b = self.controller.get_button(8)

        if (not a and not b) or (a and b):
            return (1, 0, 1500) # TODO: Update for no turn

        power = 90 * math.sqrt(axis0**2 + axis1**2)
        turn = (450 * axis0) + 1500

        return (a, power, turn)

    def getConfigDescription(self):
        return description 
