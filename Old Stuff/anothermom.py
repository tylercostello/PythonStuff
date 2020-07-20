from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
spydata=si.get_data('pcg' , start_date = '12/27/2018')
shdata=si.get_data('sh' , start_date = '12/27/2018')
mlist=[]
xaxis=[]
plist=[]
shlist=[]
period=12
lines=252
for x in range(period,lines):
    xaxis.append(x)
#print(spydata)
#print(spydata.iloc[248,3])
for x in range(period,lines):
  #print(x)
  temp=spydata.iloc[x,3]
  plist.append(temp)
  temp=shdata.iloc[x,3]
  shlist.append(temp)
for x in range(period,lines):
  #print(x)
  temp=spydata.iloc[x,3]-spydata.iloc[(x-period),3]
  temp2=(spydata.iloc[x,3]/spydata.iloc[(x-period),3])*100
  mlist.append(temp)
#print(mlist)

#print(plist)
# plotting the points
#plt.plot(xaxis, mlist)
plt.plot(xaxis, plist)
#plt.plot(xaxis, plist)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
#plt.title('Momentum')
plt.title('Price')

# function to show the plot

#print(spydata)
#print(si.get_live_price("spy"))

#threshold=-1.13
threshold=0
#maxthresh=-3
#max=0

money=100000
spyshares=0
shshares=0
#print(shdata)
#print(threshold)
for x in range(period,lines):
    #print(x)
    if mlist[x-period]>threshold and spyshares==0:
        money=money+shlist[x-period]*shshares
        shshares=0
        spyshares=math.floor(money/plist[x-period])
        money=money-plist[x-period]*spyshares
        print("Day ",x)
        print("+")
        print("spyshares ",spyshares)
        print("shshares ",shshares)
        print("Price ",plist[x-period])
        print("Price ",shlist[x-period])
        print("Net Worth ",money+plist[x-period]*spyshares+shlist[x-period]*shshares)
    if mlist[x-period]<threshold and spyshares!=0:
        money=money+plist[x-period]*spyshares
        spyshares=0
        shshares=math.floor(money/shlist[x-period])
        money=money-shlist[x-period]*shshares
        print("Day ",x)
        print("-")
        print("spyshares ",spyshares)
        print("shshares ",shshares)
        print("Price ",plist[x-period])
        print("Price ",shlist[x-period])
        print("Net Worth ",money+plist[x-period]*spyshares+shlist[x-period]*shshares)


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
print("Holding ",math.floor(100000/spydata.iloc[0,3])*plist[len(plist)-1])
#plt.show()
