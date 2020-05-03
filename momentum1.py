from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
spydata=si.get_data('sh' , start_date = '12/27/2018')
#shdata=si.get_data('sh' , start_date = '12/27/2018')
mlist=[]
xaxis=[]
plist=[]
maxlist=[]
period=12
lines=252
z=-2
while z<=2:
    xaxis.append(z)
    z=z+0.001
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

# function to show the plot

#print(spydata)
#print(si.get_live_price("spy"))

threshold=-2
maxthresh=-2
max=0
while threshold<=2:
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
    maxlist.append(money)
    if money>max:
        max=money
        maxthresh=threshold
    threshold=threshold+0.001
    """print(8*plist[len(plist)-1]-8*plist[0])"""
print(max)
print(maxthresh)
#print(math.floor(1000/spydata.iloc[0,3])*plist[len(plist)-1])
#print(math.floor(1000/spydata.iloc[0,3])*plist[0])

print(math.floor(1000/spydata.iloc[0,3])*plist[len(plist)-1])
#print((math.floor(1000/spydata.iloc[0,3])*plist[len(plist)-1])-(math.floor(1000/spydata.iloc[0,3])*plist[0]))
#print(8*plist[len(plist)-1]-8*plist[0])
plt.plot(xaxis, maxlist)
#plt.plot(xaxis, plist)
#plt.plot(xaxis, plist)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Max')
#plt.title('Price')
#plt.show()
