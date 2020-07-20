import talib
import Bakker
from yahoo_fin import stock_info as si
from talib import MA_Type
import matplotlib.pyplot as plt
import math
import csv
import json
import pandas as pd


#retrieving data
boringdata=si.get_data('SPY' , start_date = '01/01/2009')
spydata=si.get_data('SPXL' , start_date = '01/01/2009')
shortdata=si.get_data('SPXS' , start_date = '01/01/2009')
spydata['MOM'] = talib.MOM(spydata['close'], timeperiod=12)
buylist=[]
selllist=[]
#creating arrays
plist=[]
bplist=[]
mlist=[]
shortplist=[]
xaxis=[]
#print(spydata)
for x in range (12):
    buylist.append(None)
    selllist.append(None)
for x in range (len(spydata)):
    xaxis.append(x)
for x in range (len(boringdata)):
    bplist.append(boringdata.iloc[x,3])
for x in range (len(spydata)):
    plist.append(spydata.iloc[x,3])
for x in range (len(shortdata)):
    shortplist.append(shortdata.iloc[x,3])
#print(plist)
for x in range (12,len(spydata)):
    mlist.append(spydata.iloc[x,7])
#print(mlist)
shares=0
shortshares=0
money=100000

#print(x)
#print(spydata)
for x in range (12,len(plist)):
    #print(x)

    if (mlist[x-12]>-2):
        selllist.append(None)
        if shares==0:
            money=money+shortshares*shortplist[x]
            print(money)
            shortshares=0
            shares=math.floor(money/plist[x])
            money=money-plist[x]*shares
            buylist.append(plist[x])
        else:
            buylist.append(None)

    elif (mlist[x-12]<-2):
        buylist.append(None)
        if shares!=0:
            money=money+shares*plist[x]
            print(money)
            shares=0
            selllist.append(plist[x])
            #shortshares=math.floor(money/shortplist[x])
            money=money-shortplist[x]*shortshares
        else:
            selllist.append(None)
    else:
        buylist.append(None)
        selllist.append(None)



money=money+plist[len(plist)-1]*shares+shortshares*shortplist[len(shortplist)-1]
print("Momentum",money)
print("Holding 3x",math.floor(100000/bplist[12])*bplist[len(bplist)-1]+(100000-math.floor(100000/bplist[12])*bplist[12]))
print("Holding 1x",math.floor(100000/plist[12])*plist[len(plist)-1]+(100000-math.floor(100000/plist[12])*plist[12]))
plt.subplot(2, 1, 1)
plt.plot(xaxis, plist)

plt.plot(xaxis,buylist, 'go')
plt.plot(xaxis,selllist, 'ro')

plt.show()
