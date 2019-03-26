from configuration import Configuratoin


class Config4(Configuration):

    def __init__(self):
        Configuration.__init__(self)

    def resolveReadings(self, axis0, axis1):
        z = self.controller.get_button(7)
        r = self.controller.get_button(5)

        if (not z and not r) or (z and r):
            return (1, 1, 1)

        power = 254 * math.sqrt(axis0**2 + axis2**2)
        # turn = 

        return (z, power, turn)

    def getConfigDescription(self):
        return "Axis (Joysick) + Z for forward and R for reverse."
