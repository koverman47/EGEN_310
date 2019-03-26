from configuration import Configuration


class Config1(Configuration):

    def __init__(self):
        Configuration.__init__(self)

    def resolveReadings(self, axis0, axis1):
        for_rev = 1 if axis1 < 0 else 0
        power = 254 * math.sqrt(axis0**2 + axis**2)
        # turn = 
    
        return (for_rev, power, turn)

    def getConfigDescription(self):
        return "Only Axis (Joystick) Control."
