import pandas as pd

data = [0, 0, 0 , 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
val = 1
addr = data.index(val)
addr = str(addr)
if addr in range(0, 15):
    addr = 1
    reg_addr = 1
    reg_addr = int(reg_addr)
    print(reg_addr)

else:
    print('Not in Address Byte' )