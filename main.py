#!/usr/bin/env python3

import sys
import time
import paramiko
import pygame
from tkinter import *
from app import App

# SSH Data
host = "zeropythirty"
ip = "10.152.149.177"
user = "pi"
passw = "pi"


try:
    '''
    ' Construct SSH Client
    ' Default host key policy
    '''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=user, password=passw)
except BadHostKeyException:
    print("Host could not be found.")
    sys.exit(0)
except AuthenticationException:
    print("Host could not be found")
    sys.exit(0)
except SSHException as e:
    print(e)
    print("Unkown SSH error.")
    sys.exit(0)
except OSError as e:
    print(e)
except:
    print("Whoopsie doosie")

'''
' Construct Tkinter root object
' Construct application
'''
root = Tk()
app = App(root, 640, 480)
try:
    '''
    ' Start pigpio service on host
    '''
    ssh.exec_command("sudo pigpiod")
    '''
    ' Run Host reader
    '''
    result = ssh.exec_command("./EGEN_310/reader.py")
    while True:
        '''
        ' Update GUI
        ' Grabs GUI events
        '''
        root.update()

        '''
        ' Get Joystick Events
        ' Compute user commands
        '''
        events = pygame.event.get()
        data = app.configurations[app.selected].controller.read(events)

        '''
        ' Don't write to host if no updates
        '''
        if not data:
            continue

        '''
        ' Write to stdin over ssh
        ' Flush stdin
        '''
        result[0].write(data + "\n")
        result[0].flush()
except KeyboardInterrupt as e:
    print(e)
except NotImplementedError as e:
    print(e)
except SSHException as e:
    print(e)
    if result:
        print(result)
    else:
        print("Unkown SSH error.")
    print("Unkown SSH error.")
except AttributeError as e:
    print(e)
except:
    print(sys.exc_info()[0])
finally:
    '''
    ' Write exit message to stdin
    '''
    result[0].write("exit")

    '''
    ' Close SSH Tunnel
    '''
    ssh.close()
    sys.exit("Done!")






