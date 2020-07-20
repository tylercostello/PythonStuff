from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

# Dow Jones
param = {
    'q': "AAPL", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "NASDAQ", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "1M" # Period (Ex: "1Y" = 1 year)
}
# get price data (return pandas dataframe)
df = get_price_data(param)
length=(df.shape[0])-1
print(df.ix[length])
