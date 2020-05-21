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

#exchange rates between currencies; default to currency is USD

def convert_currency(fr_curr,to_curr='USD'):
    #import pandas as bear
    #from alpha_vantage.foreignexchange import ForeignExchange #https://alpha-vantage.readthedocs.io/en/latest/genindex.html
    #keys = 'BGDF14R9D6NKLQ19'
    
    output_format = ForeignExchange(key=keys, output_format='pandas')
    z = output_format.get_currency_exchange_rate(from_currency = fr_curr, to_currency  = to_curr)
    z[0].reset_index(inplace=True)
    z[0].columns = ['index','From_Currency Code','From_Currency Name','To_Currency Code','To_Currency Name','Exchange Rate','Last Refreshed','Time Zone','Bid Price','Ask Price']

    exch_rate=float(z[0]['Exchange Rate'].to_string(index=False))
    
    return exch_rate

# function call
#convert_currency('EUR')
#convert_currency('INR','EUR')
