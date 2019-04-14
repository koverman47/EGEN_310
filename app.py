#!/usr/bin/env python3

from nav import Nav
from configurations import *
from tkinter import *
import tkinter.simpledialog as SD
import tkinter.messagebox as MB
#Others
#from threading import Thread
import _thread
import pygame
import time
from mythread import MT


class App(Frame):

    def __init__(self, master=None, width=640, height=480):
        Frame.__init__(self, master)
        self.master = master
        self.configurations = []
        self.selected = 0
        self.init_window(width, height)

        # Add this shit to the configuration bindings
        #oy = MB.askyesno("Verify Selection", "Select this configuration?")
        #print(oy)
        # Add above

        self.configure_grid()
        self.configure_menu_bar() #TODO
        self.configure_side_bar() #TODO
        self.configure_main_panel() #TODO - camera feed in main panel once started?
        self.mt = MT(self.listen)
        self.mt.start()

    def init_window(self, width, height):
        self.master.geometry("%sx%s" % (width, height))
        self.master.title("RC Car")
        name = SD.askstring("Welcome!", "What is your name?")
        if name:
            self.master.title(name + "'s RC Car")
        self.pack(fill=BOTH, expand=True)

    def configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

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

    def configure_side_bar(self):
        self.configurations.append(Nav(frame=self, controller=config1.Config1()))
        self.configurations.append(Nav(frame=self, controller=config2.Config2()))
        self.configurations.append(Nav(frame=self, controller=config3.Config3()))
        self.configurations.append(Nav(frame=self, controller=config4.Config4()))
        for c in range(4):
            self.configurations[c].config(text=self.configurations[c].controller.name, borderwidth=3, relief="raised")
            self.configurations[c].grid(row=c, column=0, stick=N+W+E+S)
            self.configurations[c].bind("<Button-1>", lambda e, i=c: self.set_config(i))
        self.configurations[self.selected].config(bg="blue", relief="sunken")

    def configure_main_panel(self):
        pass

    def listen(self):
        pygame.init()
        j = pygame.joystick.Joystick(0)
        j.init()
        print("Initialized", j.get_numaxes())
        try:
            while True:
                events = pygame.event.get()
                for e in events:
                    if event.type == pygame.JOYBUTTONDOWN:
                        print("Button Pressed")
                        for b in range(10):
                            print(b, j.get_button(b))
                print(j.get_axis(0), j.get_axis(1), j.get_axis(2))
                print(j.get_button(7), j.get_button(6))
                time.sleep(1)
        except KeyboardInterrupt:
            j.quit()
        finally:
            print("Finally")


    def set_config(self, c):
        if MB.askyesno("Verify Choice", self.configurations[c].controller.description + " Is this the configuration you want?"):
            self.configurations[self.selected].config(bg="white", relief="raised")
            self.configurations[c].config(bg="blue", relief="sunken")
            self.selected = c

    def exit(self):
        self.mt._stopevent.set()

if __name__ == "__main__":
    root = Tk()
    app = App(root, 640, 480)
    root.mainloop()

