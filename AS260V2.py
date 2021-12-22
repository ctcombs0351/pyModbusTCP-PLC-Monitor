import pandas as pd
import pyModbusTCP
from datetime import datetime 
import time
import socket
import websockets 
import threading
import asyncio

print('Let us begin')

PORT = 1234
SERVER = 'localhost'
ADDR = (SERVER, PORT)
HEADER = 10
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'Fuck Off'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('client created')
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

# Alias Datetime's Current Time
dt = datetime.now()
# Store Current Date and Shift for Filename 
date = dt.strftime('%A-%d-%m-%Y-%p')
# Store Current Time 
t = str(dt.strftime('%H:%M:%S'))

# Instantiate DataFrames From Master Files
df1 = pd.read_csv('AS260FaultLog.csv')
df2 = pd.read_csv('AS260LogicTable.csv')

# Assign a Variable Name to Store User Input 
num = int(input())

# Assign a Variable Name for the Location Value in Logic Table CSV
logic = str(df2['Logic Identifier'].values[num])

# Modify Value in Fault Log Table Under the Time Column 
df1.at[0, 'Time'] = t

# Assign Variable for Fault Time Value to Store in Fault Log
fault_time = df1.at[0, 'Time']

# Build String to Store New Fault Log with Current Date
f1 = str(date)
f2 = '.csv'
file_name = str(f1 + f2)
df1.to_csv(file_name)

print(logic)
print(file_name)
send(logic)
send(DISCONNECT_MESSAGE)
