from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
spydata=si.get_data('spy' , start_date = '12/27/2018')
plist=[]
period=12
xaxis=[]
for x in range(period,252):
    xaxis.append(x)
#print(spydata)
#print(spydata.iloc[248,3])
for x in range(period,252):
  #print(x)
  temp=spydata.iloc[x,3]
  plist.append(temp)
#print(mlist)


# plotting the points
plt.plot(xaxis, plist)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Price')

# function to show the plot
plt.show()
#print(spydata)
#print(si.get_live_price("spy"))
