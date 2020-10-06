import time, requests

def print_all_pairs():
  r = requests.get("https://api.binance.com/api/v3/ticker/price")
  print(r.json())

def find_price(pair):
  r = requests.get(f"https://api.binance.com/api/v3/ticker/price?{pair}") #{'code': -1104, 'msg': "Not all sent parameters were read; read '0' parameter(s) but was sent '1'."}
  print(r.json())
