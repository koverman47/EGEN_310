#!/usr/bin/env python3

import sys

f = open("out.log", "w")
counter = 0
try:
    while counter < 1:
        counter += 1
        var = input()
        f.write(var + "\n")
except:
    f.write(sys.exc_info()[0] + "\n")
    f.write("An error has occurred")
finally:
    f.write("Done")
    f.close()
    sys.exit(0)
