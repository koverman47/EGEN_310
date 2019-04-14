#!/usr/bin/env python3

import sys
import paramiko
import time
import pygame

host = "zeropythirty"
ip = "10.152.247.52"
user = "pi"
passw = "pi"

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
except SSHException:
    print("Unkown SSH error.")
    sys.exit(0)

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

ssh.exec_command("./EGEN_310/reader.py")
print("Start")
try:
    while True:
        result = None
        #print("blep")
        #result = ssh.exec_command("echo " + j.get_axis(0) + " " + j.get_button(7))
        #result = ssh.exec_command("echo a >> EGEN_310/out.log")
        result = ssh.exec_command("echo a")
        #result[0].write("echo a")
except KeyboardInterrupt as e:
    print(e)
except NotImplementedError as e:
    print(e)
except SSHException as e:
    print(e)
    if result:
        print(result.readline())
        pass
    else:
        print("Unkown SSH error.")
except Exception as e:
    print(e)
finally:
    ssh.close()
    sys.exit(0)
