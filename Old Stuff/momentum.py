from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
spydata=si.get_data('spy' , start_date = '01/01/2019')
mlist=[]
xaxis=[]
plist=[]
alist=[]
period=12
lines=len(spydata.index)
print(lines)

#print(spydata)
#print(spydata.iloc[248,3])
for x in range(period,lines):
  #print(x)
  temp=spydata.iloc[x,3]
  plist.append(temp)
for x in range(period,lines):
  #print(x)
  temp=spydata.iloc[x,3]-spydata.iloc[(x-period),3]
  temp2=((spydata.iloc[x,3]/spydata.iloc[(x-period),3])-1)*250
  mlist.append(temp2)
#print(mlist)
for x in range(len(mlist)-1):
    alist.append(mlist[x+1]-mlist[x])
for x in range(len(alist)):
    xaxis.append(x)
#print(plist)
# plotting the points
plt.plot(xaxis, alist)
#plt.plot(xaxis, mlist)
#plt.plot(xaxis, plist)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
#plt.title('Momentum')
plt.title('Acceleration')
# function to show the plot

#print(spydata)
#print(si.get_live_price("spy"))

money=1000
shares=0
threshold=1
for x in range(period,lines):
    #print(x)
    if alist[x-period-1]>threshold and shares==0:
        shares=math.floor(money/plist[x-period])
        money=money-plist[x-period]*shares
        print(x)
        print("+")
        print(shares)
        print(plist[x-period])
        print(money+plist[x-period]*shares)
    if alist[x-period-1]<-threshold and shares!=0:
        money=money+plist[x-period]*shares
        shares=0
        print(x)
        print("-")
        print(shares)
        print(plist[x-period])
        print(money+plist[x-period]*shares)

if shares!=0:
    money=money+plist[x-period]*shares
    shares=0
    #print("-")
print(money)
print(math.floor(1000/spydata.iloc[0,3])*plist[len(plist)-1]+1000%spydata.iloc[0,3])
plt.show()
