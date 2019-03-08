#!/usr/bin/env python3

import hid
import time

vend = 9
prod = 6

h = hid.device()
h.open(vend, prod)
h.set_nonblocking(1)

start = time.time()

i = 0
while (time.time() - start) < 10:
    i += 1
    try:
        d = h.read(i)
        print(d)
    except:
        pass
    finally:
        time.sleep(0.1)
h.close()

