import math
import pygame


class Configuration():

    def __init__(self, controller):
        self.controller = controller
        self.name = "Configuration"
        self.power = 0
        self.for_rev = 1
        self.turn = 1500

    def read(self, events):
        axis0 = round(self.controller.get_axis(0), 2)
        axis1 = round(self.controller.get_axis(1), 2)

        result = self.resolveReadings(axis0, axis1, events)

        if not result:
            return
        result = list(result)
        if result[1] < 0:
            result[1] = 0
        elif result[1] > 100:
            result[1] = 100
        assert result[0] in [0, 1]
        assert result[1] >= 0
        assert result[1] <= 100
        assert result[2] >= 1000
        assert result[2] <= 2000

        return str(result[0]) + "|" + str(int(result[1])) + "|" + str(int(result[2]))

    def resolveReadings(self):
        raise NotImplementedError("Method 'resolveReadings' not implemented.")

    def getConfigDescription(self):
        raise NotImplementedError("Method 'getConfigDescription' not implemented")

    def close(self):
        self.controller.quit()
