from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest

# no keys required
client = CryptoHistoricalDataClient()

symbol="BTC/USD"
# single symbol request
request_params = CryptoLatestQuoteRequest(symbol_or_symbols=symbol)
import time
while True:
    latest_quote = client.get_crypto_latest_quote(request_params)

    # must use symbol to access even though it is single symbol
    print(latest_quote[symbol].timestamp,latest_quote[symbol].bid_price,latest_quote[symbol].ask_price)
    time.sleep(1)
