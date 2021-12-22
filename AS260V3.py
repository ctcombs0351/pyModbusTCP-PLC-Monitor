import websockets
import asyncio
import pandas as pd
from datetime import datetime
import time

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
t = str(dt.strftime('%H:%M:%S'))
min = int(dt.strftime('%M')) * 60
sec = int(dt.strftime('%S'))
ft = min + sec

df1 = pd.read_csv('AS260LogicTable.csv')
df2 = pd.read_csv('AS260FaultLog.csv')
df3 = pd.read_csv('AS260ProductionLog.csv')

num = int(input())

logic = str(df1['Logic Identifier'].values[num])
time.sleep(2)
df2.at[0, 'Start Time'] = t 
df2.at[1, logic] = 0

df3.at[0, 'Start Time'] = t

f1 = str(date)
f2 = '.csv'
file_name_fault = str('FaultLog-' + f1 + f2)
df2.to_csv(file_name_fault)

file_name_production = str('ProductionLog-' + f1 + f2)
df3.to_csv(file_name_production)

print(logic)
print(file_name_fault)
print(file_name_production)

asyncio.run(send(logic))
