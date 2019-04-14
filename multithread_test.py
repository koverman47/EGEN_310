#!/usr/bin/env python3

from threading import Thread
from tkinter import *
from app import App


class MyThread(Thread):

    def __init__(self, funx, arg):
        Thread.__init__(self)
        self.funx = funx
        self.arg = arg

    def run(self):
        self.funx(self.arg)

def printer():
    print("Apples")

def makeRoot():
    root = Tk()
    self.app = App(root)
    root.mainloop()

#root = Tk()
#app = App(root)
t2 = MyThread(makeRoot)
t1 = MyThread(printer)

t1.start()
t2.start()
t1.join()
t2.join()
