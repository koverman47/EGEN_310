#!/usr/bin/env python3

import usb

for dev in usb.core.find(find_all=True):
    print("Device: ", dev)

busses = usb.busses()
for bus in busses:
    devices = bus.devices
    for dev in devices:
        print("Product: 0x%04x\nVendor: 0x%04x" % (dev.idProduct, dev.idVendor))
