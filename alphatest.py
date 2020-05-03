#from alpha_vantage.timeseries import TimeSeries
import csv
import json
#ts = TimeSeries(key='4G0QOOO1JVKLRWM2')
import pandas as pd
data = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SPY&interval=1min&outputsize=full&apikey=4G0QOOO1JVKLRWM2&datatype=csv')
data=data.iloc[::-1]
print(data)
# Get json object with the intraday data and another with  the call's metadata
#data = ts.get_intraday('SPY','1min','csv')
#spamReader = csv.reader(open(data, newline=''), delimiter=' ', quotechar='|')
#for row in spamReader:
#    print(', '.join(row))
#mylist=data.split('"')
#print(mylist)
#print(data)
#print(json.dumps(data, indent=4))
