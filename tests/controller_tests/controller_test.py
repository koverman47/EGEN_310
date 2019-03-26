#!/usr/bin/env python3

import usb
import sys


def main(string):
    #print(string)
    device = usb.core.find(idVendor=0x0079, idProduct=0x0006)
    #print(type(device))

    device.set_configuration()

    endpoint = device[0][(0,0)][0]
    print(device)

    data = None
    while True:
        device.reset()
        try:
            data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
            rxdata = ''.join([chr(x) for x in data])
            print(data)
            print(rxdata)
        except usb.core.USBError as e:
            data = None
            print(e)
            sys.exit(0)
            if e.args == ('Operation timed out',):
                continue
        except KeyboardInterrupt:
            print("Exiting")
            sys.exit(0)
'''
'''
if __name__ == "__main__":
    main("Main called")
