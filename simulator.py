#!/usr/bin/python3

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    count = 0
    while True:
        count = count + 1
        adc = int(random.random() * 4096)
        distance = int(random.random() * 10000)
        await websocket.send('{"count": '+str(count)+', "adc": '+str(adc)+', "distance": '+str(distance)+'  }')
        await asyncio.sleep(1)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
