import Bakker
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
import csv
import json
import pandas as pd
def momentum(df, n):
    """

    :param df: pandas.DataFrame
    :param n:
    :return: pandas.DataFrame
    """
    M = pd.Series(df['MA_2'].diff(n), name='Momentum_' + str(n))
    df = df.join(M)
    return df
shon=False
xaxis=[]
plist=[]
shlist=[]
mlist=[]
mdlist=[]
smalist=[]
emalist=[]
buylist=[]
selllist=[]
shbuylist=[]
shselllist=[]
spydata=si.get_data('EURUSD=X' , start_date = '06/30/2018')
shdata=si.get_data('sh' , start_date = '06/30/2008')
smapd=Bakker.moving_average(spydata,2)
emapd=Bakker.exponential_moving_average(spydata,30)
mpd=momentum(smapd,12)

for x in range (len(mpd.index)):
    smalist.append(mpd.iloc[x,7])
for x in range (len(emapd.index)):
    emalist.append(emapd.iloc[x,7])
for x in range (len(mpd.index)):
    plist.append(mpd.iloc[x,3])
for x in range (len(shdata.index)):
    shlist.append(shdata.iloc[x,3])
for x in range (len(mpd.index)):
    mlist.append(mpd.iloc[x,8])
for x in range (len(mlist)):
    xaxis.append(x)
for x in range (1,len(mlist)):
    mdlist.append(mlist[x]-mlist[x-1])
plt.subplot(2, 1, 1)
plt.plot(xaxis, plist)
plt.plot(xaxis, emalist)
#plt.plot(xaxis, smalist)
plt.title('Trading')
buylist.append(None)
buylist.append(None)
shbuylist.append(None)
shbuylist.append(None)
selllist.append(None)
selllist.append(None)
shselllist.append(None)
shselllist.append(None)
shares=0
shorts=0
money=100000
shares=math.floor(money/plist[0])
money=money-plist[0]*shares
dist=1
"""for x in range (len(mlist)):
    if mlist[x]>0 and shares==0:
        shares=math.floor(money/plist[x])
        money=money-plist[x]*shares
        plt.plot(x,plist[x], 'go')
    if mlist[x]<0 and shares!=0:
        money=money+plist[x]*shares
        shares=0
        plt.plot(x,plist[x], 'ro')"""

for x in range (2,len(smalist)):
    #if smalist[x-1]<smalist[x] and smalist[x-1]<smalist[x-2] and shares==0:
    if mlist[x-1]<mlist[x] and mlist[x-1]<mlist[x-2] and shares==0:
    #if mlist[x-1]<mlist[x] and mlist[x-1]<mlist[x-2] and  smalist[x-1]<smalist[x] and smalist[x-1]<smalist[x-2] and shares==0:
    #if smalist[x-1]>smalist[x] and shares==0:
    #if smalist[x-dist]<smalist[x] and smalist[x-dist]<smalist[x-2*dist] and mdlist[x-dist]>0 and shares==0:
    #if smalist[x-dist]<smalist[x] and smalist[x-dist]<smalist[x-2*dist] and shares==0:
    #if smalist[x-dist]<smalist[x] and smalist[x-dist]<smalist[x-2*dist] and mlist[x-dist]>0 and shares==0:
    #if smalist[x-dist]<smalist[x] and smalist[x-dist]<smalist[x-2*dist] and shares==0:
    #if smalist[x-1]>smalist[x] and mdlist[x-1]>0 and shares==0:

        #print("up")
        if shon:
            money=money+shlist[x]*shorts
            shorts=0
            shselllist.append(shlist[x])
        shares=math.floor(money/plist[x])
        money=money-plist[x]*shares
        buylist.append(plist[x])

    else:
        buylist.append(None)
        if shon:
            shselllist.append(None)
        #plt.plot(x,plist[x], 'go')
    #if smalist[x-1]>smalist[x] and smalist[x-1]>smalist[x-2] and shares!=0:
    if mlist[x-1]>mlist[x] and mlist[x-1]>mlist[x-2] and shares!=0:
    #if mlist[x-1]>mlist[x] and mlist[x-1]>mlist[x-2] and smalist[x-1]>smalist[x] and smalist[x-1]>smalist[x-2] and shares!=0:
    #if smalist[x-1]>smalist[x] and smalist[x-1]>smalist[x-2] and shares!=0:
    #if smalist[x-1]<smalist[x] and shares!=0:
    #if smalist[x-dist]>smalist[x] and smalist[x-dist]>smalist[x-2*dist] and mdlist[x-dist]<0 and shares!=0:
    #if smalist[x-dist]>smalist[x] and smalist[x-dist]>smalist[x-2*dist] and shares!=0:
    #if smalist[x-dist]>smalist[x] and smalist[x-dist]>smalist[x-2*dist] and mlist[x-dist]<0 and shares!=0:
    #if smalist[x-dist]>smalist[x] and smalist[x-dist]>smalist[x-2*dist] and shares!=0:
        #print("down")
    #if smalist[x-1]<smalist[x] and (mdlist[x-dist]<0 or mlist[x-1]<0) and shares!=0:
    #if smalist[x-1]<smalist[x] and  mdlist[x-1]<0 and shares!=0:
        money=money+plist[x]*shares
        shares=0
        if shon:
            shorts=math.floor(money/shlist[x])
            money=money-shlist[x]*shorts
            shbuylist.append(shlist[x])
        #plt.plot(x,plist[x], 'ro')
        selllist.append(plist[x])

    else:
        selllist.append(None)
        if shon:
            shbuylist.append(None)

"""
for x in range (2,len(emalist)):
    #if emalist[x-1]<emalist[x] and emalist[x-1]<emalist[x-2] and shares==0:
    #if mlist[x-1]<mlist[x] and mlist[x-1]<mlist[x-2] and shares==0:
    #if mlist[x-1]<mlist[x] and mlist[x-1]<mlist[x-2] and  emalist[x-1]<emalist[x] and emalist[x-1]<emalist[x-2] and shares==0:
    #if emalist[x-1]>emalist[x] and shares==0:
    #if emalist[x-dist]<emalist[x] and emalist[x-dist]<emalist[x-2*dist] and mdlist[x-dist]>0 and shares==0:
    #if emalist[x-dist]<emalist[x] and emalist[x-dist]<emalist[x-2*dist] and shares==0:
    if emalist[x-dist]<emalist[x] and emalist[x-dist]<emalist[x-2*dist] and mlist[x-dist]>0 and shares==0:
    #if emalist[x-dist]<emalist[x] and emalist[x-dist]<emalist[x-2*dist] and shares==0:
    #if emalist[x-1]>emalist[x] and mdlist[x-1]>0 and shares==0:

        #print("up")
        if shon:
            money=money+shlist[x]*shorts
            shorts=0
            shselllist.append(shlist[x])
        shares=math.floor(money/plist[x])
        money=money-plist[x]*shares
        buylist.append(plist[x])

    else:
        buylist.append(None)
        if shon:
            shselllist.append(None)
        #plt.plot(x,plist[x], 'go')
    #if emalist[x-1]>emalist[x] and emalist[x-1]>emalist[x-2] and shares!=0:
    #if mlist[x-1]>mlist[x] and mlist[x-1]>mlist[x-2] and shares!=0:
    #if mlist[x-1]>mlist[x] and mlist[x-1]>mlist[x-2] and emalist[x-1]>emalist[x] and emalist[x-1]>emalist[x-2] and shares!=0:
    #if emalist[x-1]>emalist[x] and emalist[x-1]>emalist[x-2] and shares!=0:
    #if emalist[x-1]<emalist[x] and shares!=0:
    #if emalist[x-dist]>emalist[x] and emalist[x-dist]>emalist[x-2*dist] and mdlist[x-dist]<0 and shares!=0:
    #if emalist[x-dist]>emalist[x] and emalist[x-dist]>emalist[x-2*dist] and shares!=0:
    if emalist[x-dist]>emalist[x] and emalist[x-dist]>emalist[x-2*dist] and mlist[x-dist]<0 and shares!=0:
    #if emalist[x-dist]>emalist[x] and emalist[x-dist]>emalist[x-2*dist] and shares!=0:
        #print("down")
    #if emalist[x-1]<emalist[x] and (mdlist[x-dist]<0 or mlist[x-1]<0) and shares!=0:
    #if emalist[x-1]<emalist[x] and  mdlist[x-1]<0 and shares!=0:
        money=money+plist[x]*shares
        shares=0
        if shon:
            shorts=math.floor(money/shlist[x])
            money=money-shlist[x]*shorts
            shbuylist.append(shlist[x])
        #plt.plot(x,plist[x], 'ro')
        selllist.append(plist[x])

    else:
        selllist.append(None)
        if shon:
            shbuylist.append(None)
"""
money=money+plist[len(plist)-1]*shares+shlist[len(shlist)-1]*shorts
print("Momentum",money)
print("Holding ",math.floor(100000/plist[0])*plist[len(plist)-1]+(100000-math.floor(100000/plist[0])*plist[0]))

#print(mpd)

plt.plot(xaxis,buylist, 'go')
plt.plot(xaxis,selllist, 'ro')
plt.subplot(2, 1, 2)
#plt.plot(xaxis, mlist)
if shon:
    plt.plot(xaxis, shlist)
    plt.plot(xaxis,shselllist, 'ro')
    plt.plot(xaxis,shbuylist, 'go')
plt.show()
