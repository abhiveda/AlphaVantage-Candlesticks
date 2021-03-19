import plotly.graph_objects as go
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
x = input("Enter the Ticker Symbol ")

api_key = 'H1TIQBI1DQEE4I63'

ts = TimeSeries(key=api_key, output_format='pandas')

i = 1
while i==1:
    data=ts.get_intraday(symbol=f"{x}", interval='1min', outputsize='full')
    data.to_csv(f"{x}.csv")
    time.sleep(60.0)

df = pd.read_csv(f'{x}.csv')
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
fig.show()
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
x = input("Enter the Ticker Symbol ")

api_key = 'H1TIQBI1DQEE4I63'

ts = TimeSeries(key=api_key, output_format='pandas')

i = 1
while i==1:
    data=ts.get_intraday(symbol=f"{x}", interval='1min', outputsize='full')
    data.to_csv(f"{x}.csv")
    time.sleep(60.0)

df = pd.read_csv(f'{x}.csv')
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
fig.show()
import plotly.graph_objects as go
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
x = input("Enter the Ticker Symbol ")

api_key = 'H1TIQBI1DQEE4I63'

ts = TimeSeries(key=api_key, output_format='pandas')

i = 1
while i==1:
    data=ts.get_intraday(symbol=f"{x}", interval='1min', outputsize='full')
    data.to_csv(f"{x}.csv")
    time.sleep(60.0)

df = pd.read_csv(f'{x}.csv')
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
fig.show()