import alpaca_trade_api as tradeapi
import key

def convert_watchlist():
    stock_list = ['AAPL', 'TSLA', 'AMZN', 'GOOGL']
    api = tradeapi.REST(key.API_KEY, key.SECRET_KEY, key.base_url)
    watch_list = []

    for stock in stock_list:
        data = api.get_asset(stock)
        symbol = data.__getattr__('symbol')
        exchange = data.__getattr__('exchange')

        x = str(exchange + ' :' + symbol)
        watch_list.append(x)

    return watch_list