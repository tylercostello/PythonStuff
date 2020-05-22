import talib
import Bakker
from yahoo_fin import stock_info as si
from talib import MA_Type
import matplotlib.pyplot as plt
import math
import csv
import json
import pandas as pd
import tensorflow as tf
import numpy


#retrieving data

spydata=si.get_data('SPY' , start_date = '04/05/2015', end_date='04/05/2018')
testdata=si.get_data('SPY' , start_date = '04/05/2018')
prices=spydata['close'].to_numpy()
testprices=testdata['close'].to_numpy()
for x in range(len(prices)):
    prices[x]=prices[x]/400
for x in range(len(testprices)):
    testprices[x]=testprices[x]/400




#print(prices)
answer=[]
testanswer=[]
testanswer.append(1)
answer.append(1)

for x in range(1,len(prices)):
    if (prices[x]-prices[x-1]>0):
        answer.append(1)
    else:
        answer.append(0)
for x in range(1,len(testprices)):
    if (testprices[x]-testprices[x-1]>0):
        testanswer.append(1)
    else:
        testanswer.append(0)
zeroCount=0
oneCount=0
for x in range(len(answer)):
    if (answer[x]==1):
        oneCount=oneCount+1
    if (answer[x]==0):
        zeroCount=zeroCount+1
print(zeroCount)
print(oneCount)
#print(answer)
answer=numpy.asarray(answer)
testanswer=numpy.asarray(testanswer)
#print(answer)
spydata['MOM'] = talib.MOM(spydata['close'], timeperiod=12)
#print("here")
#print(len(testdata['close']))
testdata['MOM'] =talib.MOM(testdata['close'], timeperiod=12)
#print(len(testdata['MOM']))
mom=spydata['MOM'].to_numpy()
testmom=testdata['MOM'].to_numpy()

for x in range (0,12):
    mom[x]=0.1
for x in range (0,12):
    testmom[x]=0.1
xaxis=[]
for x in range(len(spydata)):
    xaxis.append(x)
customMOM=[]
for x in range (0,12):
    customMOM.append(0.1)
for x in range(12,len(spydata)):
    customMOM.append((spydata.iloc[x,3]/spydata.iloc[x-12,3])*100)
#adam=tf.keras.optimizers.Adam(learning_rate=0.0001, beta_1=0.9, beta_2=0.999, amsgrad=False)
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(1,)),
    tf.keras.layers.Dense(256, activation=tf.nn.relu),
	tf.keras.layers.Dense(256, activation=tf.nn.relu),
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
testmom=testmom.reshape(-1,1)
mom=mom.reshape(-1,1)
testprices=testprices.reshape(-1,1)
prices=prices.reshape(-1,1)
answer=answer.reshape(-1,1)
testanswer=testanswer.reshape(-1,1)
model.summary()
#model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])
#model.compile(loss='sparse_categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
twoMom=[]
twoMom.append(mom[44])
twoMom.append(mom[45])
twoAnswer=[]
twoAnswer.append(answer[44])
twoAnswer.append(answer[45])
twoMom=numpy.asarray(twoMom)
twoAnswer=numpy.asarray(twoAnswer)
#print(mom)
#print(answer)
print(mom)
print(twoMom)
print(answer)
print(twoAnswer)
print(twoMom[0:2:1].shape)
print(mom.shape)
print(answer.shape)
#model.fit(twoMom[0:2:1],twoAnswer[0:2:1],epochs=10)
print(prices[43])
print(prices[44])
print(answer[44])
#model.fit(mom[100::1],answer[100::1],epochs=1000000)
#print(len(testprices))
#print(len(testanswer))
#print(len(testmom))

model.evaluate(testmom[44],  testanswer[44], verbose=2)
print(model.predict(testmom[42]))
print(testanswer[42])
print(model.predict(testmom[43]))
print(testanswer[43])
print(model.predict(testmom[44]))
print(testanswer[44])

#predictions = model(prices[:1]).numpy()
#print(predictions)
plt.plot(xaxis, spydata['MOM'])

#plt.plot(xaxis, spydata['MOM'])

#plt.show()
