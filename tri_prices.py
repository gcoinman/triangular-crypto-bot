import time, requests

PAIRS = ['ETHBTC', 'BTCUSDT', 'ETHUSDT']

#find conversion between each pair

def get_prices():
    ethbtc = float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHBTC").json()['price'])
    btcusdt = float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()['price'])
    usdteth = 1 / float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT").json()['price'])
    return ethbtc, btcusdt, usdteth

def check_triangle(prices):
    second = prices[0] * prices[1]
    third = second * prices[2]
    return third

prices = get_prices()
tri = check_triangle(prices)
print(prices)
print(f"1 > {tri}")