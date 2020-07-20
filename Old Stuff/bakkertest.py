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
Tlist=[]
dlist=[]
ddlist=[]
def true_strength_index(df, r, s):
    """Calculate True Strength Index (TSI) for given data.

    :param df: pandas.DataFrame
    :param r:
    :param s:
    :return: pandas.DataFrame
    """
    M = pd.Series(df['close'].diff(1))
    aM = abs(M)
    EMA1 = pd.Series(M.ewm(span=r, min_periods=r).mean())
    aEMA1 = pd.Series(aM.ewm(span=r, min_periods=r).mean())
    EMA2 = pd.Series(EMA1.ewm(span=s, min_periods=s).mean())
    aEMA2 = pd.Series(aEMA1.ewm(span=s, min_periods=s).mean())
    TSI = pd.Series(EMA2 / aEMA2, name='TSI_' + str(r) + '_' + str(s))
    df = df.join(TSI)
    return df
newList=true_strength_index(spydata,25,13)
#adxlist=Bakker.average_directional_movement_index(spydata,14,14)
#print(adxlist)
#-0 Tlist -1 dlist -2 ddlist
for x in range (len(spydata.index)):
    xaxis.append(x)
for x in range (len(spydata.index)):
    Tlist.append(newList.iloc[x,7])
#for x in range (len(newList.index)-1):
#    dlist.append(newList.iloc[x+1,7]-newList.iloc[x,7])
#dlist.append(None)
dlist.append(None)
for x in range (1,len(newList.index)):
    dlist.append(newList.iloc[x,7]-newList.iloc[x-1,7])
ddlist.append(None)
ddlist.append(None)
for x in range (2,len(newList.index)):
    ddlist.append(dlist[x]-dlist[x-1])

#for x in range (len(newList.index)-2):
    #ddlist.append(dlist[x+1]-dlist[x])
#ddlist.append(None)
#ddlist.append(None)
"""plt.plot(xaxis, ddlist)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
#plt.title('Momentum')
plt.title('TSID2')
plt.show()"""

plt.subplot(3, 1, 1)
plt.plot(xaxis, Tlist)
plt.title('TSI')

plt.subplot(3, 1, 2)
plt.plot(xaxis, dlist)

plt.subplot(3, 1, 3)
plt.plot(xaxis, ddlist)

plt.show()
