import datetime 
import time

import pandas as pd
import pandas_ta as ta
from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest,StockBarsRequest
from alpaca.trading.client import *
from alpaca.trading.requests import *
import credentials as cs
from alpaca.data.timeframe import TimeFrame

api_key = cs.api_key
secret_key = cs.secret_key



tickers = ["BTC/USD",'ETH/USD']
crypto_client = CryptoHistoricalDataClient()
trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=True, url_override=None)

# contract_objects={}
# for tick in tickers:
#     print(Crypto(tick,exchange,currency))
#     contract_objects[tick]=ib.qualifyContracts(Crypto(tick,exchange,currency))[0]
# print(contract_objects)

def get_historical_data(ticker_contract):

    request_params = CryptoBarsRequest(
                            symbol_or_symbols=ticker_contract,
                            timeframe=TimeFrame.Minute,
                            start=datetime.datetime(2024, 5, 20),
                            end=datetime.datetime(2024, 6, 16)
                    )

    bars = crypto_client.get_crypto_bars(request_params)


    # convert to pandas dataframe:
    df = bars.df
    # print(df)
    df['sma1']=ta.sma(df.close,20)
    df['sma2']=ta.sma(df.close,50)
    
    return df


def main_strategy_code():

    print("inside main strategy")
    positions = trade_client.get_all_positions()
    pos_df=pd.DataFrame([dict(position) for position in positions])
    print(pos_df)

    # see all open orders
    req = GetOrdersRequest(
        status = QueryOrderStatus.ALL,
        symbols = tickers
    )
    open_orders = trade_client.get_orders(req)
    open_orders
    ord_df=pd.DataFrame([dict(ord) for ord in open_orders])
    print(ord_df)


    for ticker in tickers:
        print('ticker name is',ticker,'################')
 

        hist_df=get_historical_data(ticker)
        print(hist_df)
        print(hist_df.close.iloc[-1])

        acct = trade_client.get_account()
        capital=float(dict(acct).get('cash'))
        quantity=int((capital/10)/hist_df.close.iloc[-1])  
        print(quantity)

import datetime
current_time=datetime.datetime.now()
print(current_time)

print(datetime.datetime.now())
#start time
start_hour,start_min=19,0
#end time
end_hour,end_min=20,50
start_time=datetime.datetime(current_time.year,current_time.month,current_time.day,start_hour,start_min)
end_time=datetime.datetime(current_time.year,current_time.month,current_time.day,end_hour,end_min)
print(start_time)
print(end_time)

candle_size=60

while datetime.datetime.now()<end_time:
    now = datetime.datetime.now()
    print(now)
    seconds_until_next_minute = candle_size - now.second+1
    print(seconds_until_next_minute)
    # Sleep until the end of the current minute
    time.sleep(seconds_until_next_minute)

    # Run your function
    main_strategy_code()