from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
import csv
import json
import pandas as pd
#ts = TimeSeries(key='4G0QOOO1JVKLRWM2')
#spydata=si.get_data('amzn' , start_date = '12/27/2014')
spydata=pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=1min&outputsize=full&apikey=4G0QOOO1JVKLRWM2&datatype=csv')
#shdata=si.get_data('sh' , start_date = '12/27/2014')
shdata=pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SPY&interval=1min&outputsize=full&apikey=4G0QOOO1JVKLRWM2&datatype=csv')
#print(spydata)
mlist=[]
xaxis=[]
plist=[]
shlist=[]
period=12
#lines=1258
#shape=spydata.shape
#print(len(spydata.index))
lines=len(spydata.index)
for x in range(period,lines):
    xaxis.append(x)
for x in range(period,lines):
  x=len(spydata.index)-x
  temp=spydata.iloc[x,3]
  plist.append(temp)
  temp=shdata.iloc[x,3]
  shlist.append(temp)
for x in range(period,lines):
  x=len(spydata.index)-x
  temp=spydata.iloc[x,3]-spydata.iloc[(x-period),3]
  temp2=((spydata.iloc[x,3]/spydata.iloc[(x-period),3])-1)*250
  mlist.append(temp2)
#plt.plot(xaxis, mlist)
plt.plot(xaxis, plist)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
#plt.title('Momentum')
plt.title('Price')
#threshold=-1.13
threshold=0
#maxthresh=-3
#max=0
money=100000
spyshares=0
shshares=0
spyshares=math.floor(money/plist[0])
money=money-plist[0]*spyshares
print(plist[0])
for x in range(period,lines):
    #if mlist[x-period]>threshold and spyshares==0:
    if mlist[x-period]>0.6 and spyshares==0:
        #money=money+shlist[x-period]*shshares
        #shshares=0
        spyshares=math.floor(money/plist[x-period])
        money=money-plist[x-period]*spyshares
        print("Day ",x)
        print("+")
        print("spyshares ",spyshares)
        print("shshares ",shshares)
        print("Price ",plist[x-period])
        print("Price ",shlist[x-period])
        print("Net Worth ",money+plist[x-period]*spyshares+shlist[x-period]*shshares)
        plt.plot(x,plist[x-period], 'go')
    #if mlist[x-period]<threshold and spyshares!=0:
    if mlist[x-period]<-1.1 and spyshares!=0:
        money=money+plist[x-period]*spyshares
        spyshares=0
        #shshares=math.floor(money/shlist[x-period])
        #money=money-shlist[x-period]*shshares
        print("Day ",x)
        print("-")
        print("spyshares ",spyshares)
        print("shshares ",shshares)
        print("Price ",plist[x-period])
        print("Price ",shlist[x-period])
        print("Net Worth ",money+plist[x-period]*spyshares+shlist[x-period]*shshares)
        plt.plot(x,plist[x-period], 'ro')
money=money+plist[x-period]*spyshares+shlist[x-period]*shshares
spyshares=0
shshares=0
print("-")
print("Momentum ",money)
"""if money>max:
    max=money
    maxthresh=threshold
threshold=threshold+0.001"""
"""print(8*plist[len(plist)-1]-8*plist[0])"""
#print(max)
#print(maxthresh)
#print(8*plist[len(plist)-1]-8*plist[0])
#print(8*plist[len(plist)-1])
print("Holding ",math.floor(100000/spydata.iloc[len(spydata.index)-1,3])*plist[len(plist)-1])
#print("Holding ",math.floor(100000/spydata.iloc[0,3])*plist[len(plist)-1])
plt.show()
