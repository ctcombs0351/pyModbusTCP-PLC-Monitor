import pandas as pd
import pyModbusTCP
import datetime
import time

# Store Current Date for Filename 
date = datetime.date.today()
# Store Current Time 
t = str(datetime.datetime.now().time())

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
