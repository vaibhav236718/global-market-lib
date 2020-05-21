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

# search quote value by symbol; returns quotes in USD

def quote_val_by_symbol(symba):
    #import pandas as bear
    #from alpha_vantage.timeseries import TimeSeries #https://alpha-vantage.readthedocs.io/en/latest/genindex.html
    #keys = 'BGDF14R9D6NKLQ19' #get free API Key here: https://www.alphavantage.co/support/#api-key

    output_format = TimeSeries(key=keys, output_format='pandas')
    x = output_format.get_symbol_search(keywords=symba)
    x[0].reset_index(inplace=True)
    x[0].columns = ['date','symbol','name','type','region','marketOpen','marketClose','timezone','currency','matchScore']
    
    base_currency = x[0][x[0]['symbol']==symba]['currency'].to_string(index=False)
    base_currency = base_currency.replace(" ","")
    rate = convert_currency(base_currency)
       
    output_format = TimeSeries(key=keys, output_format='pandas')
    y = output_format.get_quote_endpoint(symbol=symba)
    y[0].reset_index(inplace=True)
    y[0].columns = ['index','symbol','open','high','low','price','volume','latest trading day','previous close','change','change percent']
    y[0]
    
    quote_in_usd=y[0]
    quote_in_usd['open']  = (float(quote_in_usd['open']) * rate )
    quote_in_usd['high']  = (float(quote_in_usd['high']) * rate )
    quote_in_usd['low']   = (float(quote_in_usd['low']) * rate  )
    quote_in_usd['price'] = (float(quote_in_usd['price']) * rate)
    
    return quote_in_usd

# function call
#quote_val_by_symbol('RELIANCE.NSE')


