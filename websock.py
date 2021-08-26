#!/usr/bin/env python3

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

import serial




async def time(websocket, path):
    print("Start serial")
    ser = serial.Serial('/dev/ttyACM0',timeout=0.5)  # open serial port

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
                    distance = 0
                    print(adc)
                    await websocket.send('{"count": '+str(count)+', "adc": '+str(adc)+', "distance": '+str(distance)+'  }')
        
        #await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
