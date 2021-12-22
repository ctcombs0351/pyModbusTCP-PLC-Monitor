import pandas as pd
from datetime import datetime
import time
import pyModbusTCP
from pyModbusTCP.client import ModbusClient

dt = datetime.now()
#
date = dt.strftime('%A-%d-%m-%Y-%p')
#
t = str(dt.strftime('%H:%M:%S'))
#
min = int(dt.strftime('%M')) * 60
#
sec = int(dt.strftime('%S'))
#
fault_time = min + sec
#
df1 = pd.read_csv('AS260LogicTable.csv')
#
df2 = pd.read_csv('A1.csv', index_col = [0])
# 
df3 = pd.read_csv('A2.csv', index_col = [0])
#
c = ModbusClient(host = '192.168.250.1', port = 502, unit_id = 1, auto_open = True)

val = 1

def logic(num):
	logic = str(df1['Logic Identifier'].values[num])

def fault(num):
	logic = str(df1['Logic Identifier'].values[num])
	df2.at[1, logic] = t
	print(logic)

def sixteen03():
	c.open()
	data = c.read_holding_registers(256, 16)
	if data == 'None':
		data = c.read_holding_registers(256, 16)
		time.sleep(0.1)
	else:
		addr = data.index(val)
		logic_addr = int('146' + addr)
		logic = str(df1['Logic Identifier'].values[logic_addr])
		return logic

def close_file():
	f1 = str(date)
	f2 = '.csv'
	file_name_fault = str('FaultLog-' + f1 + f2)
	df2.to_csv(file_name_fault, index = False)
	file_name_production = str('ProductionLog-' + f1 + f2)
	df3.to_csv(file_name_production, index = False)
	print(file_name_production)
	print(file_name_fault)

