#!/usr/bin/env python3

from nav import Nav
from configurations import *
from tkinter import *
import tkinter.simpledialog as SD
import tkinter.messagebox as MB
import pygame
import time
import sys


class App(Frame):

    '''
    ' Initialize main application frame
    '''
    def __init__(self, master=None, width=640, height=480):
        Frame.__init__(self, master)
        self.master = master
        self.configurations = []
        self.selected = 0
        self.init_window(width, height)

        self.configure_grid()
        self.configure_menu_bar()
        self.configure_pygame()
        self.configure_side_bar()
        self.configure_main_panel() #TODO - camera feed in main panel once started?

    '''
    ' Set window geometry
    ' Get user name
    '''
    def init_window(self, width, height):
        self.master.geometry("%sx%s" % (width, height))
        self.master.title("RC Car")
        name = SD.askstring("Welcome!", "What is your name?")
        if name:
            self.master.title(name + "'s RC Car")
        self.pack(fill=BOTH, expand=True)

    '''
    ' Set 2x6 grid layout - equal weights
    '''
    def configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    '''
    ' Set menu bar
    ' If OSX - top of screen
    ' Else top of window
    '''
    def configure_menu_bar(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        f = Menu(menu)
        conf = Menu(menu)

        f.add_command(label="Exit", command=self.exit)
        for c in range(4):
            conf.add_command(label="Configuration " + str(c + 1), command=lambda: self.set_config(c))

        menu.add_cascade(label="File", menu=f)
        menu.add_cascade(label="Configuration", menu=conf)

    '''
    ' Create configurations corresponding to controller options
    '''
    def configure_side_bar(self):
        self.configurations.append(Nav(frame=self, controller=config1.Config1(self.joystick)))
        self.configurations.append(Nav(frame=self, controller=config2.Config2(self.joystick)))
        self.configurations.append(Nav(frame=self, controller=config3.Config3(self.joystick)))
        self.configurations.append(Nav(frame=self, controller=config4.Config4(self.joystick)))
        for c in range(4):
            self.configurations[c].config(text=self.configurations[c].controller.name, borderwidth=3, relief="raised")
            self.configurations[c].grid(row=c, column=0, stick=N+W+E+S)
            self.configurations[c].bind("<Button-1>", lambda e, i=c: self.set_config(i))
        self.configurations[self.selected].config(bg="blue", relief="sunken")

    '''
    ' Video Feed
    '''
    def configure_main_panel(self):
        pass

    '''
    ' Callback for setting new controller configuration
    '''
    def set_config(self, c):
        if MB.askyesno("Verify Choice", self.configurations[c].controller.description + " Is this the configuration you want?"):
            self.configurations[self.selected].config(bg="white", relief="raised")
            self.configurations[c].config(bg="blue", relief="sunken")
            self.selected = c

    '''
    ' Establish pygame thread and intitialize the joystick controller
    '''
    def configure_pygame(self):
        pygame.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def exit(self):
        '''
        ' Close joystick controller and exit
        '''
        self.joystick.quit()
        sys.exit("Exiting App")



