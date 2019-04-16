#!/usr/bin/env python3

import sys
import time
import paramiko
import pygame
from tkinter import *
from app import App

host = "zeropythirty"
#ip = "10.152.183.190"
#ip = "10.152.247.52"
ip = "10.152.180.3"
user = "pi"
passw = "pi"

root = Tk()
app = App(root, 640, 480)


try:
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
except:
    print("Whoopsie doosie")

try:
    ssh.exec_command("sudo pigpiod")
    #result = ssh.exec_command("./EGEN_310/tests/reader_test.py")
    result = ssh.exec_command("./EGEN_310/reader.py")
    while True:
        root.update()
        events = pygame.event.get()
        data = app.configurations[app.selected].controller.read()
        result[0].write(data + "\n") # write to stdin
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
except AttributeError as e:
    print(e)
except:
    print(sys.exc_info()[0])
finally:
    result[0].write("exit")    
    ssh.close()
    sys.exit("Done!")






