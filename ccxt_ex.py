import ccxt
from config import *

exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': secret
})

# ohlcv = ex.fetch_ohlcv('BTC/USDT', '5m')
balances = exchange.fetch_balance()
for balance in balances:
    if isinstance(balances[balance], dict) and 'total' in balances[balance] and balances[balance]['total'] > 0:
        print(balance, balances[balance])

