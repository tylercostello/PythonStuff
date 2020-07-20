import talib
import Bakker
from yahoo_fin import stock_info as si
from talib import MA_Type
import matplotlib.pyplot as plt
import math
import csv
import json
import pandas as pd
xaxis=[]
SARlist=[]
plist=[]
buylist=[]
selllist=[]
MOMlist=[]
MACDlist=[]
smaMACDlist=[]
timeperiod=12
looper=13
bbandList=[]
shortShares=0
#for x in range (looper):
#    buylist.append(None)
#    selllist.append(None)



spydata=si.get_data('UPRO' , start_date = '01/01/2015')

spydata['SAR'] = talib.SAR(spydata['high'], spydata['low'], acceleration=0.02, maximum=0.2)
spydata['MOM'] = talib.MOM(spydata['close'], timeperiod=12)
spydata['MACD'], spydata['MACDSIGNAL'], spydata['MACDHIST'] = talib.MACD(spydata['close'], fastperiod=12, slowperiod=26, signalperiod=9)
spydata['smaMACD']=talib.SMA(spydata['MACDHIST'], 3)
spydata['UPPER'], spydata['MIDDLE'], spydata['LOWER'] = talib.BBANDS(spydata['close'], timeperiod=25, matype=MA_Type.DEMA)
#print(spydata)
SARlist.append(None)
SARlist.append(None)
for x in range (len(spydata)):
    xaxis.append(x)
for x in range (len(spydata)):
    MACDlist.append(spydata.iloc[x,11])
for x in range (len(spydata)):
    bbandList.append(spydata.iloc[x,14])
for x in range (len(spydata)):
    smaMACDlist.append(spydata.iloc[x,12])
for x in range (len(spydata)):
    plist.append(spydata.iloc[x,3])
for x in range (2,len(spydata)):
    SARlist.append(spydata.iloc[x,7])
for x in range (timeperiod):
    MOMlist.append(None)
for x in range (timeperiod,len(spydata)):
    MOMlist.append(spydata.iloc[x,8])
print(spydata)
shares=0
money=100000
shares=math.floor(money/plist[0])
money=money-plist[0]*shares
for x in range (0,len(plist)):
    
    #if SARlist[x-1]<plist[x-1] and shares==0:
    #if SARlist[x-1]<plist[x-1] and SARlist[x-2]<plist[x-2] and SARlist[x-3]<plist[x-3] and shares==0:
    #if SARlist[x-1]>plist[x-1] and shares==0:
    #if MOMlist[x-1]>0 or SARlist[x-1]<plist[x-1]:
    if MACDlist[x-1] <0 and MACDlist[x]>0:
    #if plist[x-2]<bbandList[x-2] and plist[x-1]>bbandList[x-1]:
    #if plist[x-1]<bbandList[x-1] and plist[x]>bbandList[x]:


        if shares==0:
            money=money-shortShares*plist[x]
            #print("Money ",money)
            shortShares=0
            shares=math.floor(money/plist[x])
            money=money-plist[x]*shares
            #print("Money ",money)
            buylist.append(plist[x])
            #print('buy',x)
        else:
            buylist.append(None)
        #print("Money ",money)

    else:
        buylist.append(None)
    #if SARlist[x-1]>plist[x-1] and shares!=0:
    #if SARlist[x-1]>plist[x-1] and SARlist[x-2]>plist[x-2] and SARlist[x-3]>plist[x-3] and shares!=0:
        #if MOMlist[x-1]<0 or SARlist[x-1]>plist[x-1]:
    #if plist[x-2]>bbandList[x-2] and plist[x-1]<bbandList[x-1]:
    #if plist[x-1]>bbandList[x-1] and plist[x]<bbandList[x]:
    if MACDlist[x-1] >0 and MACDlist[x]<0:
        if shares!=0:
            money=money+plist[x]*shares
            #print("Money ",money)
            shares=0
            selllist.append(plist[x])
            shortShares=math.floor(money/plist[x])
            money=money+plist[x]*shortShares
            #print("Money ",money)
            buyPrice = plist[x]
            #print('sell',x)
        else:
            selllist.append(None)
    else:
        selllist.append(None)
    print("Money ",money)

print(shortShares)
money=money+plist[len(plist)-1]*shares-shortShares*plist[len(plist)-1]

print("MACD",money)
print("Holding ",math.floor(100000/plist[0])*plist[len(plist)-1]+(100000-math.floor(100000/plist[0])*plist[0]))
plt.subplot(2, 1, 1)
plt.plot(xaxis, plist)
#plt.plot(xaxis, SARlist)
plt.plot(xaxis,buylist, 'go')
plt.plot(xaxis,selllist, 'ro')
#plt.plot(xaxis, smalist)
#plt.title('Trading')
#plt.subplot(2, 1, 2)
#plt.plot(xaxis, MACDlist)
plt.show()
