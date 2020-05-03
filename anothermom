from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
spydata=si.get_data('spy' , start_date = '12/27/2009')
mlist=[]
xaxis=[]
plist=[]
period=12
lines=2517
for x in range(period,lines):
    xaxis.append(x)
#print(spydata)
#print(spydata.iloc[248,3])
for x in range(period,lines):
  #print(x)
  temp=spydata.iloc[x,3]
  plist.append(temp)
for x in range(period,lines):
  #print(x)
  temp=spydata.iloc[x,3]-spydata.iloc[(x-period),3]
  temp2=(spydata.iloc[x,3]/spydata.iloc[(x-period),3])*100
  mlist.append(temp)
#print(mlist)

#print(plist)
# plotting the points
plt.plot(xaxis, mlist)
#plt.plot(xaxis, plist)
#plt.plot(xaxis, plist)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Momentum')
#plt.title('Price')

# function to show the plot

#print(spydata)
#print(si.get_live_price("spy"))

threshold=-3
maxthresh=-3
max=0
while threshold<=3:
    money=1000
    shares=0
    #print(threshold)
    for x in range(period,lines):
        #print(x)
        if mlist[x-period]>threshold and shares==0:
            shares=math.floor(money/plist[x-period])
            money=money-plist[x-period]*shares
            """print(x)
            print("+")
            print(shares)
            print(plist[x-period])
            print(money+plist[x-period]*shares)"""
        if mlist[x-period]<threshold and shares!=0:
            money=money+plist[x-period]*shares
            shares=0
            """print(x)
            print("-")
            print(shares)
            print(plist[x-period])
            print(money+plist[x-period]*shares)"""

    if shares!=0:
        money=money+plist[x-period]*shares
        shares=0
        """print("-")"""
    #print(money)
    if money>max:
        max=money
        maxthresh=threshold
    threshold=threshold+0.001
    """print(8*plist[len(plist)-1]-8*plist[0])"""
print(max)
print(maxthresh)
#print(8*plist[len(plist)-1]-8*plist[0])
#print(8*plist[len(plist)-1])
print(math.floor(1000/spydata.iloc[0,3])*plist[len(plist)-1])
    #plt.show()
