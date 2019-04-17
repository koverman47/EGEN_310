#!/usr/bin/env python3

import sys
import traceback

f = open("EGEN_310/tests/out.log", "w")
counter = 0
try:
    while True:
        #f.write(str(counter) + "\n")
        #counter += 1
        var = input()
        if var == "exit":
            f.write("Chunky monkey\n")
            break
        #f.write(var + "\n")
        data = var.rstrip().split("|")
        f.write(data[0] + " " + data[1] + " " + data[2] + "\n")
except:
    f.write(traceback.format_exc() + "\n")
finally:
    f.write("Done")
    f.close()
    sys.exit(0)
