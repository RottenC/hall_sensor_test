#!/usr/bin/env python3

import serial
import datetime
import time
import sys

ser = serial.Serial('/dev/ttyACM0',timeout=0.5)  # open serial port

try:
    while True:
        s = ser.read(4096)
        if len(s) != 0:
            d = str(s,'utf-8')
            chunks = d.split('\n')

            for val in chunks:
                if val != '':
                    serial_data = val.split(':')
                    timestamp = int(serial_data[0])
                    count = int(serial_data[1])
                    adc = int(serial_data[2])
                    print(adc)


except KeyboardInterrupt:
    f.close()
    ser.close()
    print("")
    print('File closed.')

