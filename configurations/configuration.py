import math


class Configuration():

    def __init__(self, controller):
        self.controller = controller
        self.name = "Configuration"

    def read(self):
        axis0 = round(self.controller.get_axis(0), 2)
        axis1 = round(self.controller.get_axis(1), 2)

        for_rev, power, turn = self.resolveReadings(axis0, axis1)

        assert for_rev in [0, 1]
        assert power >= 0
        assert power <= 255
        assert turn >= 1000
        assert turn <= 2000

        return str(for_rev) + "|" + str(int(power)) + "|" + str(int(turn))

    def resolveReadings(self):
        raise NotImplementedError("Method 'resolveReadings' not implemented.")

    def getConfigDescription(self):
        raise NotImplementedError("Method 'getConfigDescription' not implemented")

    def close(self):
        self.controller.quit()
