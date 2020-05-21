import numpy as np
from matplotlib import pyplot as plt

plt.style.use('bmh')
#plt.style.available

# create plot comparison between n companies

def plot_comparison(com_list,range_begin,range_end):
    time = TimeSeries(key=keys, output_format='pandas')
    i=0
    
    for com in com_list:
        data = time.get_daily(symbol=com, outputsize='compact')
        data[0].reset_index(inplace=True)
        data[0].columns = ['date-time', 'open', 'high', 'low', 'close', 'volume']
        
        output_format = TimeSeries(key=keys, output_format='pandas')
        y = output_format.get_symbol_search(keywords=com)
        y[0].reset_index(inplace=True)
        y[0].columns = ['date','symbol','name','type','region','marketOpen','marketClose','timezone','currency','matchScore']
        
        # convert base currency to USD
        base_currency = y[0][y[0]['symbol']==com]['currency'].to_string(index=False)
        base_currency = base_currency.replace(" ","")
        rate = convert_currency(base_currency)
        #data[0]['close'] = bear.to_float(data[0]['date-time'])*rate
        
        data[0]['date-time'] = bear.to_datetime(data[0]['date-time'])
        mask = (data[0]['date-time'] >= range_begin) & (data[0]['date-time'] <= range_end)

        accross = 0.20
        shift = i*accross
        i = i+1
        
        #replace x-axis value with respective legends, add rotation
        plt.xticks(data[0][mask].index, data[0][mask]['date-time'],rotation=90)
        plt.bar(data[0][mask].index+shift, data[0][mask]['close'], width = accross)
        #plt.plot(data[0][mask].index+shift, data[0][mask]['close']*rate)
        
    plt.legend(com_list)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Value Comparison')
    plt.show()
        

        
#plt.style.use('seaborn')
#x = ['IBM','AAPL','RELIANCE.NSE']
#x = ['AAPL','RELIANCE.NSE']
#y = '2020-05-01'
#z = '2020-05-10'

#plot_comparison(x,y,z)        
