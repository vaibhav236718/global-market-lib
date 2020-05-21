import pandas as bear
from alpha_vantage.timeseries import TimeSeries #https://alpha-vantage.readthedocs.io/en/latest/genindex.html
from alpha_vantage.foreignexchange import ForeignExchange #https://alpha-vantage.readthedocs.io/en/latest/genindex.html

keys = 'BGDF14R9D6NKLQ19'

#why do we need multiple keys ?
#ValueError: Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency.

# for random from multiple keys in key files
# import random
# lines = open('keys').read().splitlines()
# print(lines)
# key = random.choice(lines) 
# print(key)

# find latest value from available intraday data

def latest_from_intraday(ticker):
    #import pandas as bear
    #from alpha_vantage.timeseries import TimeSeries #https://alpha-vantage.readthedocs.io/en/latest/genindex.html
    #keys = 'BGDF14R9D6NKLQ19' #get free API Key here: https://www.alphavantage.co/support/#api-key

    bear.set_option('display.max_rows',100)
    time = TimeSeries(key=keys, output_format='pandas')
    data = time.get_intraday(symbol=ticker, interval='1min', outputsize='full')

    data[0].reset_index(inplace=True)
    data[0].columns = ['date-time', 'open', 'high', 'low', 'close', 'volume']


    from datetime import datetime
    fmt = '%Y-%m-%d %H:%M:%S'

    latest_record=(data[0]['date-time'] == data[0]['date-time'].max())
    last_tym=datetime.strptime(data[0][latest_record]['date-time'].to_string(index=False),fmt)
    last_val=data[0][latest_record]['close'].to_string(index=False)
    
    return (ticker,'latest intraday time and value',last_tym,last_val)

# function call
# latest_from_intraday('IBM')
