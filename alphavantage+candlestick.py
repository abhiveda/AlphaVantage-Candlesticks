import plotly.graph_objects as go
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'H1TIQBI1DQEE4I63'
print("KEEP CAPS LOCK ON AND ENTER EVERYTHING")
x = input("Enter Ticker Symbol")
ts = TimeSeries(key=api_key, output_format='pandas')

prompt = "NO"
i = 86400
c = 0
val = 1
t = ""
wait = 0
norepeater = 0
secs = 0.0
mylistcheck=[]
while i > 1:
    if norepeater != 1:
        if wait == 1:
            time.sleep(30.0)
        c = c + 1
        data, meta_data = ts.get_intraday(symbol=f'{x}', interval='1min', outputsize='full')
        date = time.localtime()
        data.to_csv(f"{x}.csv")
        df = pd.read_csv(f"{x}.csv")
        fig = go.Figure(data=[go.Candlestick(x=df['date'],
                                             open=df['1. open'],
                                             high=df['2. high'],
                                             low=df['3. low'],
                                             close=df['4. close'])])
        fig.show()
        secs = 30.0
        i = i - 1
        date_list = df['date'].tolist()
        open_list = df['1. open'].tolist()
        high_list = df['2. high'].tolist()
        low_list = df['3. low'].tolist()
        close_list = df['4. close'].tolist()
        if wait == 0:
            LoL = [date_list, open_list, high_list, low_list, close_list]
        else:
            last_element = 0
            LoL.append([date_list[last_element], open_list[last_element],
                        high_list[last_element],
                        low_list[last_element], close_list[last_element]])
            mylistcheck=[date_list[last_element], open_list[last_element],
             high_list[last_element],
             low_list[last_element], close_list[last_element]]
        print(LoL)
        print(mylistcheck)
        time.sleep(30)
    #if prompt == 'YES':
        #c = 0
        #ks = TimeSeries(key=api_key, output_format='pandas')
        #datat, meta_datat = ks.get_intraday(symbol=f"{t}", interval='1min', outputsize='compact')
        #datet = time.localtime()
        #print(datat)
        #print(datet)
        #datat.to_csv(f"{t}.csv")
        #dft = pd.read_csv(f"{t}.csv")
        #figt = go.Figure(data=[go.Candlestick(x=dft['date'],
                                              #open=dft['1. open'],
                                              #high=dft['2. high'],
                                              #low=dft['3. low'],
                                              #close=dft['4. close'])])
        #figt.show()
        #time.sleep(secs)
        #i = i - 1
        #norepeater = 0
    #if prompt != "YES":
        #if val == 1:
            #print("Enter YES if you want new Stock Graph ")
            #print("Enter anything else if you don't")
            #prompt = input("Another Stock Graph?")
        #wait = 1
    #if prompt == "YES":
        #if c == 1:
            #t = input("Enter New Ticker")
            #norepeater = 1
        #continue
    #else:
        print("OKAY")
        prompt = "NO"
        val = 0
        wait = 1
        continue
