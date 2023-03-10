import alpaca_trade_api as tradeapi
from alpaca.data import TimeFrame
import key

# create Alpaca API object with the given credentials
api = tradeapi.REST(key.API_KEY,
                    key.SECRET_KEY,
                    key.base_url)

# Call the API to get OHLC TSLA data adn store it in a dataframe
data = api.get_bars(
    symbol='TSLA',
    timeframe=TimeFrame.Minute
).df

# Get some historical data for TSLA
historical_data = api.get_bars(
    symbol='TSLA', #any symbol is acceptable if it can be found in Alpaca API
    timeframe=TimeFrame.Minute,
    start="2018-01-01T00:00:00-00:00",
    end="2018-02-01T00:00:00-00:00"
).df

print(data)
print(historical_data)