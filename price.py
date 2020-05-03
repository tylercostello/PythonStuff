import Bakker
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
import logging

# Import Third-Party
import pandas as pd
import numpy as np
spydata=si.get_data('spy' , start_date = '01/01/2019')
pd.set_option('display.max_rows', None)
#print(spydata)
xaxis=[]
plist=[]

for x in range (len(spydata.index)):
    xaxis.append(x)
for x in range (len(spydata.index)):
    plist.append(spydata.iloc[x,3])

plt.plot(xaxis, plist)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
#plt.title('Momentum')
plt.title('Price')
plt.show()
