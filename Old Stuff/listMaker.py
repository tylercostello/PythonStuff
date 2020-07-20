import talib
import Bakker
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
import csv
import json
import pandas as pd
import sys
df = pd.read_csv("constituents_csv.csv")
matrix2 = df[df.columns[0]].as_matrix()
list2 = matrix2.tolist()
#df = pd.read_csv("nasdaq.csv")
#matrix2 = df[df.columns[0]].as_matrix()
#list3 = matrix2.tolist()
failed=0
#df = pd.read_csv("companylist (1).csv")
#matrix2 = df[df.columns[0]].as_matrix()
#list3 = matrix2.tolist()
#tickerList=list2+list3
tickerList=list2
#for x in range (len(tickerList)):
#    print(tickerList[x])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

for x in range (len(tickerList)):
    #print(tickerList[x])
    try:
        stockdata=si.get_data(tickerList[x] , start_date = '01/01/2019')
        #stockdata['RSI']=talib.RSI(stockdata['close'], timeperiod=14)
        #stockdata['MOM']=talib.MOM(stockdata['close'], timeperiod=12)
        #stockdata['ADX']=talib.ADX(stockdata['high'], stockdata['low'], stockdata['close'], timeperiod=14)
        stockdata['MACD'], stockdata['MACDSIGNAL'], stockdata['MACDHIST'] = talib.MACD(stockdata['close'], fastperiod=12, slowperiod=26, signalperiod=9)
        #print(stockdata)

        #stockdata['RSI']=talib.SAR(stockdata['high'], stockdata['low'], acceleration=0.02, maximum=0.2)
        #if (float(stockdata.iloc[len(stockdata)-1]['RSI']) <= 40 and float(stockdata.iloc[len(stockdata)-1]['MOM']) >= 0):
        #if ((float(stockdata.iloc[len(stockdata)-2]['MACDSIGNAL']) < 0 and float(stockdata.iloc[len(stockdata)-1]['MACDSIGNAL']) > 0)  and float(stockdata.iloc[len(stockdata)-1]['MOM']) >= 0 and float(stockdata.iloc[len(stockdata)-1]['ADX']) > 25):
        if ((float(stockdata.iloc[len(stockdata)-2]['MACDSIGNAL']) < 0 and float(stockdata.iloc[len(stockdata)-1]['MACDSIGNAL']) > 0)):
            print(tickerList[x])
            print("winner")
            #print(float(stockdata.iloc[len(stockdata)-1]['RSI']))

        #else:
        #    print("MOM")
        #    print(float(stockdata.iloc[len(stockdata)-1]['MOM']))
        #    print("RSI")
        #    print(stockdata.iloc[len(stockdata)-1]['RSI'])
    except KeyboardInterrupt:
        sys.exit()
    except:
        failed=failed+1
        #ok
print("finished")
