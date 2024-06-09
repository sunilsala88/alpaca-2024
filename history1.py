from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest,StockBarsRequest
import credentials as cs
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
api_key = cs.api_key
secret_key = cs.secret_key

# # no keys required.
# crypto_client = CryptoHistoricalDataClient()


# print(TimeFrame.Month)

# list_of_tickers=["BTC/USD",'ETH/USD']

# for ticker in list_of_tickers:
#     request_params = CryptoBarsRequest(
#                             symbol_or_symbols=ticker,
#                             timeframe=TimeFrame.Minute,
#                             start=datetime(2024, 5, 1),
#                             end=datetime(2024, 6, 9)
#                     )

#     bars = crypto_client.get_crypto_bars(request_params)
#     print(bars)
#     # # convert to dataframe
#     print(bars.df)

    # # access bars as list - important to note that you must access by symbol key
    # # even for a single symbol request - models are agnostic to number of symbols
    # print(bars.df["BTC/USD"])
    # import pandas as pd

    # bars.df.to_csv('data.csv')



stock_client = StockHistoricalDataClient(api_key,secret_key)


print(TimeFrame.Month)

list_of_tickers=["BTC/USD",'ETH/USD']


request_params = StockBarsRequest(
                        symbol_or_symbols='AMZN',
                        timeframe=TimeFrame.Minute,
                        start=datetime(2024, 5, 1),
                        end=datetime(2024, 6, 9)
                )

bars = stock_client.get_stock_bars(request_params)
print(bars)
# # convert to dataframe
print(bars.df)