import websockets
import asyncio
import pandas as pd
from datetime import datetime
import time
import os
import AS260V4ModBus

# Establish Websocket Send Function
async def send(msg):
	async with websockets.connect('ws://192.168.43.83:8086') as websocket:
		await websocket.send(msg)

# Establish Websocket Receive Function
async def recv(msg):
	async with websockets.connect('ws://192.168.43.83:8086') as websocket:
		await websocket.send(msg)

dt = datetime.now()
date = dt.strftime('%A-%d-%m-%Y-%p')

num = int(input())

if __name__ == '__main__':
	AS260V4ModBus.fault(num)
	AS260V4ModBus.close_file()

#os.remove(file_name_production)
asyncio.run(send(AS260V4ModBus.logic))
