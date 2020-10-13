import time, requests

PAIRS = ['ETHBTC', 'BTCUSDT', 'ETHUSDT']

#find conversion between each pair

def get_prices():
    ethusdt = float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT").json()['price'])
    usdtbtc = 1 / float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()['price'])
    btceth = 1 / float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHBTC").json()['price'])
    return ethusdt, usdtbtc, btceth

def check_triangle(prices):
    second = (0.1 * prices[0]) * prices[1]
    third = second * prices[2]
    return third

while True:
    prices = get_prices()
    tri = check_triangle(prices)
    if tri >= 0.10001:
        print(prices)
        print(f"0.1 > {tri}")
        time.sleep(1)