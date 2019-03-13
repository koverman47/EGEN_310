#!/usr/bin/env python3

import paramiko
import sys
import tty
import termios


# RPi Zero w SSH Credentials
host = "zeropythirty"
ip = "10.152.183.190"
user = "pi"
passw = "pi"

# Establish SSH tunnel
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=user, password=passw)
except BadHostKeyException:
    print("Host could not be found.")
    sys.exit(0)
except AuthenticationException:
    print("Could not authenticate host.")
    sys.exit(0)
except SSHException:
    print("Unknown SSH error.")
    sys.exit(0)

# Give stdin to this script
tty.setcbreak(sys.stdin)
try:
    while True:
        result = None
        # Read and pass key over SSH tunnel
        key = ord(sys.stdin.read(1))
        result = ssh.exec_command(key)
except KeyboardInterrupt:
    pass
except SSHException:
    if result:
        print(result)
finally:
    # Return stdin to ECHO
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    old[3] = old[3] | termios.ECHO
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    # Close SSH tunnel
    ssh.close()

