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

# to find out stock info (name, symbol, market etc.)

def look_it_up(keyword):
    #import pandas as bear
    #from alpha_vantage.timeseries import TimeSeries #https://alpha-vantage.readthedocs.io/en/latest/genindex.html
    #keys = 'BGDF14R9D6NKLQ19' #get free API Key here: https://www.alphavantage.co/support/#api-key

    output_format = TimeSeries(key=keys, output_format='pandas')
    x = output_format.get_symbol_search(keywords=keyword)
    x[0].reset_index(inplace=True)
    x[0].columns = ['date','symbol','name','type','region','marketOpen','marketClose','timezone','currency','matchScore']
    x[0]
    
    return x[0]

# function call
#look_it_up('reliance')
