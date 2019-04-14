#!/usr/bin/env python3

from tkinter import Label


class Nav(Label):

    def __init__(self, frame, text=None, borderwidth=2, relief="raised", controller=None):
        Label.__init__(self, frame, text=text, borderwidth=borderwidth, relief=relief)
        self.controller = controller

