#!/usr/bin/env python3

import sys
import tty
import termios

tty.setcbreak(sys.stdin)
key = ord(sys.stdin.read(1))
print(key)

fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
old[3] = old[3] | termios.ECHO
termios.tcsetattr(fd, termios.TCSADRAIN, old)

sys.exit(0)
