import websockets
import asyncio
import pandas as pd
from datetime import datetime
import time
import os

dt = datetime.now()

# if statement for ID badge input
if __name__ == '__main__':
# extract badge number from input and establish a login time and date
#print(badge_id)
	id_num = str('ID#_12345')
	df2 = pd.read_csv('AS260FaultLog.csv')
	df3 = pd.read_csv('AS260ProductionLog.csv')
	log_time = str(dt.strftime('%H:%M:%S'))
	df2.at[0, 'Operator ID'] = id_num
	df3.at[0, 'Operator ID'] = id_num
	df2.at[0, 'Start Time'] = log_time
	df3.at[0, 'Login Time'] = log_time
	df2.to_csv('A1.csv')
	df3.to_csv('A2.csv')
	import AS260V5Modbus

num = int(input())

AS260V5Modbus.fault(num)
AS260V5Modbus.close_file()

async def send_fault(msg):
	async with websockets.connect('ws://192.168.43.83:8086') as websocket:
		await websocket.send(msg)

# Establish Websocket Receive Function
async def recv(msg):
	async with websockets.connect('ws://192.168.43.83:8086') as websocket:
		await websocket.send(msg)

# Establish Websocket Send Function
async def send_csv(msg):
	async with websockets.connect('ws://192.168.43.83:8086') as websocket:
		await websocket.send(msg)

#os.remove(file_name_production)
asyncio.run(send_fault(AS260V5Modbus.logic))
