from configuration import Configuration


class Config2(Configuration):
    
    def __init__(self):
        Configuration.__init__(self)

    def resolveReadings(self, axis1, axis2):
        z = self.controller.get_button(7)
        power = 254 * math.sqrt(axis1**2 + axis2**2)
        #turn = 

        return (z, power, turn)

    def getConfigDescription(self):
        return "Axis (Joystick) for directional control and Z to go."
