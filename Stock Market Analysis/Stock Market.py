import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# We would like a nice whitegrid behind our visualizations
sb.set_style('whitegrid')

# We will be reading stock information from Google Finance or Yahoo Finance
# Functions from pandas.io.data extract data from various Internet sources into a Data Frame
# Sources supported include: Yahoo Finance, Google Finance, World Bank, Google Analytics, etc
from pandas.io.data import DataReader
from datetime import datetime
from __future__ import division

# We will make a list of the tech stocks we want to look at
tech_list = ['AAPL', 'GOOG', 'MSFT', 'ZEN', 'AMZN']

# We set up an end and start time (a year ago from now)
end = datetime.now()
start = datetime(end.year-1, end.month, end.day)

# We create dataframes from yahoo finance
# We use globals() so then eg calling AAPL returns the dataframe for Apple
for stock in tech_list:
    globals()[stock] = DataReader(stock, 'yahoo', start, end)

# >>> ZEN.describe()
#             Open        High         Low       Close          Volume  \
# count  252.000000  252.000000  252.000000  252.000000      252.000000
# mean    22.039683   22.425262   21.628456   22.072381   849731.746032
# std      2.543808    2.551269    2.587121    2.561434   611762.662511
# min     14.930000   15.850000   14.385000   14.770000   179700.000000
# 25%     20.287501   20.677500   19.977500   20.345001   503050.000000
# 50%     21.549999   21.819999   21.265000   21.540000   714050.000000
# 75%     23.740000   24.162500   23.267500   23.662500   994975.000000
# max     27.420000   28.000000   27.160000   27.740000  4138800.000000

#        Adj Close
# count  252.000000
# mean    22.072381
# std      2.561434
# min     14.770000
# 25%     20.345001
# 50%     21.540000
# 75%     23.662500
# max     27.740000

# >>> ZEN.info()
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 252 entries, 2015-06-12 to 2016-06-10
# Data columns (total 6 columns):
# Open         252 non-null float64
# High         252 non-null float64
# Low          252 non-null float64
# Close        252 non-null float64
# Volume       252 non-null int64
# Adj Close    252 non-null float64

# We call the adjusted close column from the ZEN dataframe to visualize Zendesk's stock for the past year
Zendesk_stock_past_year = ZEN['Adj Close'].plot(legend=True, figsize=(10, 4))

# Or we can check for the past 10 years for Zendesk
globals()[tech_list[3]] = DataReader(stock, 'yahoo', datetime(end.year-10, end.month,end.day), end)
Zendesk_stock_decade = ZEN['Adj Close'].plot(legend=True, figsize=(10, 4))

# What about volume of stock traded each day for the past year?
# We set Zendesk datetime again
globals()[tech_list[3]] = DataReader(stock, 'yahoo', datetime(end.year-1, end.month,end.day), end)
Zendesk_daily_volume_traded = ZEN['Volume'].plot(legend=True, figsize=(10, 4))

# We can calculate 10, 20, 50 day moving averages
# We will create 3 separate columns on the ZEN DataFrame
# rolling_mean(DataFrame, time window)
# Then we can plot the Adj Close and the 3 new columns
ma_day = [10, 20, 50]
for ma in ma_day:
    column_name = "MA for %s days" % (str(ma))
    ZEN[column_name] = pd.rolling_mean(ZEN['Adj Close'], ma)

Zendesk_moving_averages = ZEN[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(subplots=False,figsize=(10, 4))

# We can check the daily return. Again, we make a new column using the adjusted closing price
# The Daily Return graph is in %
# We can analyse risk on the stock based on the daily return behaviour
ZEN['Daily Return'] = ZEN['Adj Close'].pct_change()
Zendesk_daily_return = ZEN['Daily Return'].plot(figsize=(10, 4), legend=True, linestyle='--',marker='o')

# Now, we want to look at the frequency distributions, so we will use a histogram
# The histogram is positively skewed so it seems like a good move
# The first one is by seaborn and the second by pandas
Zendesk_annual_return_dist0 = sb.distplot(ZEN['Daily Return'].dropna(), bins=100, color='orange')
Zendesk_annual_return_dist0.set_xlim(-0.1, 0.1)
Zendesk_annual_return_dist = ZEN['Daily Return'].hist(bins=100)

# Analyzing the returns of all the stocks in our list
# We create a dataframe from the Adjusted Closing Price from all the stocks
# And then with seaborn we can compare different stocks with correlation
closing_df = DataReader(tech_list, 'yahoo', start, end)['Adj Close']
tech_returns = closing_df.pct_change()
Amazon_Zendesk_returns = sb.jointplot('AMZN', 'ZEN', tech_returns, kind='scatter', color='seagreen')








