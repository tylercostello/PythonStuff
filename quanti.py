# Import pandas
import pandas as pd
# Import yfinance
import yfinance as yf
# Import data from yahoo finance
data = yf.download(tickers='AMZN', start='2014-01-01', end='2019-10-01')
# Drop the NaN values
data = data.dropna()
data.head()
# Import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fast')
# Plot the closing price
data.Close.plot(figsize=(10,5))
plt.grid()
#plt.show()
# Import talib
import talib
# Calculate parabolic sar
data['SAR'] = talib.SAR(data.High, data.Low, acceleration=0.02, maximum=0.2)
print(data)
# Plot Parabolic SAR with close price
data[['Close', 'SAR']][:500].plot(figsize=(10,5))
plt.grid()
plt.show()
