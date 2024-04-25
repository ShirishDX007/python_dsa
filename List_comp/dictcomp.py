#{key: value in (key, value) in dict.items() if condition}

stocks = {
    'Reliance': 2999,
    'HDFCBANK': 1525,
    'HAL': 3959,
    'GAIL': 299
}

stock_price = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(stock_price)