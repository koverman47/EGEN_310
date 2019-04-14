#!/usr/bin/env python3

from threading import Thread


class MT(Thread):

    def __init__(self, fxn):
        Thread.__init__(self)
        self.fxn = fxn

    def run(self):
        self.fxn()
