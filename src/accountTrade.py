import time, requests
import hashlib, base64, hmac, json
from urllib.parse import urljoin, urlencode

SECRET_KEY = ''
KEY = ''
BASE_URL = 'https://testnet.binance.vision/api'
headers = {
    'X-MBX-APIKEY': KEY
}

def get_server_time():
    PATH =  '/api/v1/time'
    params = None
    timestamp = int(time.time() * 1000)
    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, params=params)
    print(url)
    print(r.json())

def create_order():
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': 'ETHUSDT',
        'side': 'BUY',
        'type': 'MARKET',
        #'timeInForce': 'GTC',
        'quantity': 0.1,
        #'price': 500.0,
        'recvWindow': 60000,
        'timestamp': timestamp
    }
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    print(r.json())

def get_snapshot():
    PATH = '/api/v3/account'
    timestamp = int(time.time() * 1000)
    params = {
        'timestamp': timestamp
    }
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    print(r.json())

create_order()
get_snapshot()