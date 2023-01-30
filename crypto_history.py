from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.historical import CryptoHistoricalDataClient
import datetime

# No keys required for crypto data
client = CryptoHistoricalDataClient()
# Creating request object
request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD"],
                        timeframe=TimeFrame.Day,
                        start= datetime.datetime(2022, 7, 1), 
                        end= datetime.datetime(2022, 8, 1)
                        )

btc_bars = client.get_crypto_bars(request_params)

# Convert to dataframe
btc_bars.df

print(btc_bars)