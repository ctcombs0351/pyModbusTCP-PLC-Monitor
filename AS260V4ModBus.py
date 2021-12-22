import pandas as pd
from datetime import datetime
import time
import pyModbusTCP


dt = datetime.now()
t = str(dt.strftime('%H:%M:%S'))
min = int(dt.strftime('%M')) * 60
sec = int(dt.strftime('%S'))
ft = min + sec
date = dt.strftime('%A-%d-%m-%Y-%p')

df1 = pd.read_csv('AS260LogicTable.csv')
df2 = pd.read_csv('AS260FaultLog.csv')
df3 = pd.read_csv('AS260ProductionLog.csv')

df2.at[0, 'Start Time'] = t
df3.at[0, 'Start Time'] = t

def logic():
	logic = str(df1['Logic Identifier'].values[num])
	print(logic)

def fault(num):
	logic = str(df1['Logic Identifier'].values[num]) 
	df2.at[1, logic] = 0
	print(logic)

def close_file():
	f1 = str(date)
	f2 = '.csv'
	file_name_fault = str('FaultLog-' + f1 + f2)
	df2.to_csv(file_name_fault)
	file_name_production = str('ProductionLog-' + f1 + f2)
	df3.to_csv(file_name_production)
	print(file_name_production)
	print(file_name_fault)
