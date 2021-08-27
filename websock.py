#!/usr/bin/env python3

import asyncio
import datetime
import random
import websockets
import serial

async def time(websocket, path):
    print("Start serial")
    ser = serial.Serial('/dev/ttyACM0',timeout=0.5)  # open serial port

    while True:
        s = ser.readline()
        if len(s) != 0:
            d = str(s,'utf-8')
            serial_data = d.split(':')
            timestamp = int(serial_data[0])
            count = int(serial_data[1])
            adc = int(serial_data[2])
            distance = 0
            await websocket.send('{"count": '+str(count)+', "adc": '+str(adc)+', "distance": '+str(distance)+'  }')
        
start_server = websockets.serve(time, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
