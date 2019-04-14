from configurations.configuration import Configuration

class Config3(Configuration):
    description = "Axis (Joystick) for turn and power. A/B for forward/reverse."

    def __init__(self):
        Configuration.__init__(self)
        self.name = "Configuration 3"

    def resolveReadings(self, axis0, axis1):
        a = self.controller.get_button(6)
        b = self.controller.get_button(8)

        if (not a and not b) or (a and b):
            return (1, 1, 1) # TODO: Update for no turn

        power = 254 * math.sqrt(axis0**2 + axis1**2)
        # turn = 

        return (a, power, turn)

    def getConfigDescription(self):
        return description 
