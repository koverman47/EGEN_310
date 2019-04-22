#! /usr/bin/env python3
import vlc
import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
    from Tkinter import ttk
    from Tkinter.filedialog import askopenfilename
else:
    import tkinter as Tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename

import os
import time

class Player(Tk.Frame):
    def __init__(self, parent, title=None):
        Tk.Frame.__init__(self, parent)

        self.parent = parent

        if title == None:
            title = "tk_vlc"
        self.parent.title(title)

        # The second panel holds controls
        self.player = None
        self.videopanel = ttk.Frame(self.parent)
        self.canvas = Tk.Canvas(self.videopanel).pack(fill=Tk.BOTH,expand=1)
        self.videopanel.pack(fill=Tk.BOTH,expand=1)

        # VLC player controls
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()

        self.begin()
        self.parent.update()

    def begin(self):
        # Creation
        url = "http://10.152.242.51:8080/?action=stream"
        #self.Media = self.Instance.media_new(str(os.path.join(dirname, filename)))
        self.Media = self.Instance.media_new(url)
        self.player.set_media(self.Media)
        print("Boogula")

        self.player.set_xwindow(self.GetHandle()) # this line messes up windows

    def GetHandle(self):
        return self.videopanel.winfo_id()

    def OnTimer(self):
        if self.player == None:
            return
        length = self.player.get_length()
        dbl = length * 0.001

        tyme = self.player.get_time()
        if tyme == -1:
            tyme = 0
        dbl = tyme * 0.001

    def scale_sel(self, evt):
        if self.player == None:
            return
        nval = self.scale_var.get()
        sval = str(nval)

    def errorDialog(self, errormessage):
        Tk.tkMessageBox.showerror(self, 'Error', errormessage)

def Tk_get_root():
    if not hasattr(Tk_get_root, "root"): #(1)
        Tk_get_root.root= Tk.Tk()  #initialization call is inside the function
    return Tk_get_root.root

def _quit():
    print("_quit: bye")
    root = Tk_get_root()
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    os._exit(1)

if __name__ == "__main__":
    root = Tk_get_root()
    root.protocol("WM_DELETE_WINDOW", _quit)

    player = Player(root, title="tkinter vlc")
    root.mainloop()
