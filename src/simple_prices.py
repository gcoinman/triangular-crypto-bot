import time, requests

def print_all_pairs():
    r = requests.get("https://api.binance.com/api/v3/ticker/price")
    print(r.json())

def price(pair):
    r = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pair}")
    return float(r.json()['price'])

def price_change(pair):
    p = price(pair)
    print(p)
    while True:
        num = price(pair)
        if num != p:
            r = num-p
            change = f"{r:.9f}"
            t = time.time()
            print(f"Price: {num} | Change: {change} | Time (s): {t}")
            p = num
    return ""

price_change("ETHBTC")