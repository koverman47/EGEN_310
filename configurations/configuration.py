import pygame
import math


class Configuration():

    def __init__(self):
        pygame.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def read(self):
        axis0 = round(self.controller.get_axis(0), 2)
        axis1 = round(self.controller.get_axis(1), 2)

        for_rev, power, turn = self.resolveReadings(axis0, axis1)

        assert for_rev in [0, 1]
        assert power >= 1
        assert power <= 255
        assert turn >= 1
        assert turn <= 255

        return str(for_rev) + "|" + str(power) + "|" + str(turn)

    def resolveReadings(self):
        raise NotImplementedError("Method 'resolveReadings' not implemented.")

    def getConfigDescription(self):
        raise NotImplementedError("Method 'getConfigDescription' not implemented")

    def close(self):
        self.controller.quit()
