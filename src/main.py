import time, requests, math, threading
import hashlib, base64, hmac, json
from urllib.parse import urljoin, urlencode

SECRET_KEY = '[SECRET_KEY]'
KEY = '[KEY]'
BASE_URL = 'https://api.binance.com'
headers = {
    'X-MBX-APIKEY': KEY
}
FEE = 0.001

#Orders a pair
def order(pair, side, quantity):
    PATH = '/api/v3/order'
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': pair,
        'side': side,
        'type': 'MARKET',
        'quantity': quantity,
        'recvWindow': 60000,
        'timestamp': timestamp
    }
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, PATH)
    r = requests.post(url, headers=headers, params=params)
    print(r.json())

#Returns my account's information (balances, permissions, etc.)
def snapshot():
    PATH = '/api/v3/account'
    timestamp = int((time.time() *1000))
    params = {
        'timestamp': timestamp
    }
    query_string = urlencode(params)
    params['signature'] = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers, params=params)
    return r.json()

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

#Returns all pairs on Binance
def get_pairs():
    PATH = '/api/v3/exchangeInfo'
    url = urljoin(BASE_URL, PATH)
    r = requests.get(url, headers=headers)
    return r.json()

#All pairs on Binance exchange
PAIRS = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'QTUMETH', 'EOSETH', 'SNTETH', 'BNTETH', 'BCCBTC', 'GASBTC', 'BNBETH', 'BTCUSDT', 'ETHUSDT', 'HSRBTC', 'OAXETH', 'DNTETH', 'MCOETH', 'ICNETH', 'MCOBTC', 'WTCBTC', 'WTCETH', 'LRCBTC', 'LRCETH', 'QTUMBTC', 'YOYOBTC', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'STRATBTC', 'STRATETH', 'SNGLSBTC', 'SNGLSETH', 'BQXBTC', 'BQXETH', 'KNCBTC', 'KNCETH', 'FUNBTC', 'FUNETH', 'SNMBTC', 'SNMETH', 'NEOETH', 'IOTABTC', 'IOTAETH', 'LINKBTC', 'LINKETH', 'XVGBTC', 'XVGETH', 
'SALTBTC', 'SALTETH', 'MDABTC', 'MDAETH', 'MTLBTC', 'MTLETH', 'SUBBTC', 'SUBETH', 'EOSBTC', 'SNTBTC', 'ETCETH', 'ETCBTC', 'MTHBTC', 'MTHETH', 'ENGBTC', 'ENGETH', 'DNTBTC', 'ZECBTC', 'ZECETH', 'BNTBTC', 'ASTBTC', 'ASTETH', 'DASHBTC', 'DASHETH', 'OAXBTC', 'ICNBTC', 'BTGBTC', 'BTGETH', 'EVXBTC', 'EVXETH', 'REQBTC', 'REQETH', 'VIBBTC', 'VIBETH', 'HSRETH', 'TRXBTC', 'TRXETH', 'POWRBTC', 'POWRETH', 'ARKBTC', 'ARKETH', 'YOYOETH', 'XRPBTC', 'XRPETH', 'MODBTC', 'MODETH', 'ENJBTC', 'ENJETH', 'STORJBTC', 
'STORJETH', 'BNBUSDT', 'VENBNB', 'YOYOBNB', 'POWRBNB', 'VENBTC', 'VENETH', 'KMDBTC', 'KMDETH', 'NULSBNB', 'RCNBTC', 'RCNETH', 'RCNBNB', 'NULSBTC', 'NULSETH', 'RDNBTC', 'RDNETH', 'RDNBNB', 'XMRBTC', 'XMRETH', 'DLTBNB', 'WTCBNB', 'DLTBTC', 'DLTETH', 'AMBBTC', 'AMBETH', 'AMBBNB', 'BCCETH', 'BCCUSDT', 'BCCBNB', 'BATBTC', 'BATETH', 'BATBNB', 'BCPTBTC', 'BCPTETH', 'BCPTBNB', 'ARNBTC', 'ARNETH', 'GVTBTC', 'GVTETH', 'CDTBTC', 'CDTETH', 'GXSBTC', 'GXSETH', 'NEOUSDT', 'NEOBNB', 'POEBTC', 'POEETH', 'QSPBTC', 
'QSPETH', 'QSPBNB', 'BTSBTC', 'BTSETH', 'BTSBNB', 'XZCBTC', 'XZCETH', 'XZCBNB', 'LSKBTC', 'LSKETH', 'LSKBNB', 'TNTBTC', 'TNTETH', 'FUELBTC', 'FUELETH', 'MANABTC', 'MANAETH', 'BCDBTC', 'BCDETH', 'DGDBTC', 'DGDETH', 'IOTABNB', 'ADXBTC', 'ADXETH', 'ADXBNB', 'ADABTC', 'ADAETH', 'PPTBTC', 'PPTETH', 'CMTBTC', 'CMTETH', 'CMTBNB', 'XLMBTC', 'XLMETH', 'XLMBNB', 'CNDBTC', 'CNDETH', 'CNDBNB', 'LENDBTC', 'LENDETH', 'WABIBTC', 'WABIETH', 'WABIBNB', 'LTCETH', 'LTCUSDT', 'LTCBNB', 'TNBBTC', 'TNBETH', 'WAVESBTC', 
'WAVESETH', 'WAVESBNB', 'GTOBTC', 'GTOETH', 'GTOBNB', 'ICXBTC', 'ICXETH', 'ICXBNB', 'OSTBTC', 'OSTETH', 'OSTBNB', 'ELFBTC', 'ELFETH', 'AIONBTC', 'AIONETH', 'AIONBNB', 'NEBLBTC', 'NEBLETH', 'NEBLBNB', 'BRDBTC', 'BRDETH', 'BRDBNB', 'MCOBNB', 'EDOBTC', 'EDOETH', 'WINGSBTC', 'WINGSETH', 'NAVBTC', 'NAVETH', 'NAVBNB', 'LUNBTC', 'LUNETH', 'TRIGBTC', 'TRIGETH', 'TRIGBNB', 'APPCBTC', 'APPCETH', 'APPCBNB', 'VIBEBTC', 'VIBEETH', 'RLCBTC', 'RLCETH', 'RLCBNB', 'INSBTC', 'INSETH', 'PIVXBTC', 'PIVXETH', 'PIVXBNB', 
'IOSTBTC', 'IOSTETH', 'CHATBTC', 'CHATETH', 'STEEMBTC', 'STEEMETH', 'STEEMBNB', 'NANOBTC', 'NANOETH', 'NANOBNB', 'VIABTC', 'VIAETH', 'VIABNB', 'BLZBTC', 'BLZETH', 'BLZBNB', 'AEBTC', 'AEETH', 'AEBNB', 'RPXBTC', 'RPXETH', 'RPXBNB', 'NCASHBTC', 'NCASHETH', 'NCASHBNB', 'POABTC', 'POAETH', 'POABNB', 'ZILBTC', 'ZILETH', 'ZILBNB', 'ONTBTC', 'ONTETH', 'ONTBNB', 'STORMBTC', 'STORMETH', 'STORMBNB', 'QTUMBNB', 'QTUMUSDT', 'XEMBTC', 'XEMETH', 'XEMBNB', 'WANBTC', 'WANETH', 'WANBNB', 'WPRBTC', 'WPRETH', 'QLCBTC', 
'QLCETH', 'SYSBTC', 'SYSETH', 'SYSBNB', 'QLCBNB', 'GRSBTC', 'GRSETH', 'ADAUSDT', 'ADABNB', 'CLOAKBTC', 'CLOAKETH', 'GNTBTC', 'GNTETH', 'GNTBNB', 'LOOMBTC', 'LOOMETH', 'LOOMBNB', 'XRPUSDT', 'BCNBTC', 'BCNETH', 'BCNBNB', 'REPBTC', 'REPETH', 'REPBNB', 'BTCTUSD', 'TUSDBTC', 'ETHTUSD', 'TUSDETH', 'TUSDBNB', 'ZENBTC', 'ZENETH', 'ZENBNB', 'SKYBTC', 'SKYETH', 'SKYBNB', 'EOSUSDT', 'EOSBNB', 'CVCBTC', 'CVCETH', 'CVCBNB', 'THETABTC', 'THETAETH', 'THETABNB', 'XRPBNB', 'TUSDUSDT', 
'IOTAUSDT', 'XLMUSDT', 'IOTXBTC', 'IOTXETH', 'QKCBTC', 'QKCETH', 'AGIBTC', 'AGIETH', 'AGIBNB', 'NXSBTC', 'NXSETH', 'NXSBNB', 'ENJBNB', 'DATABTC', 'DATAETH', 'ONTUSDT', 'TRXBNB', 'TRXUSDT', 'ETCUSDT', 'ETCBNB', 'ICXUSDT', 'SCBTC', 'SCETH', 'SCBNB', 'NPXSBTC', 'NPXSETH', 'VENUSDT', 'KEYBTC', 'KEYETH', 'NASBTC', 'NASETH', 'NASBNB', 'MFTBTC', 'MFTETH', 'MFTBNB', 'DENTBTC', 'DENTETH', 'ARDRBTC', 'ARDRETH', 'ARDRBNB', 'NULSUSDT', 'HOTBTC', 'HOTETH', 'VETBTC', 'VETETH', 'VETUSDT', 'VETBNB', 'DOCKBTC', 
'DOCKETH', 'POLYBTC', 'POLYBNB', 'PHXBTC', 'PHXETH', 'PHXBNB', 'HCBTC', 'HCETH', 'GOBTC', 'GOBNB', 'PAXBTC', 'PAXBNB', 'PAXUSDT', 'PAXETH', 'RVNBTC', 'RVNBNB', 'DCRBTC', 'DCRBNB', 'USDCBNB', 'MITHBTC', 'MITHBNB', 'BCHABCBTC', 'BCHSVBTC', 'BCHABCUSDT', 'BCHSVUSDT', 'BNBPAX', 'BTCPAX', 'ETHPAX', 'XRPPAX', 'EOSPAX', 'XLMPAX', 'RENBTC', 'RENBNB', 'BNBTUSD', 'XRPTUSD', 'EOSTUSD', 'XLMTUSD', 'BNBUSDC', 'BTCUSDC', 'ETHUSDC', 'XRPUSDC', 'EOSUSDC', 'XLMUSDC', 'USDCUSDT', 'ADATUSD', 'TRXTUSD', 'NEOTUSD', 
'TRXXRP', 'XZCXRP', 'PAXTUSD', 'USDCTUSD', 'USDCPAX', 'LINKUSDT', 'LINKTUSD', 'LINKPAX', 'LINKUSDC', 'WAVESUSDT', 'WAVESTUSD', 'WAVESPAX', 'WAVESUSDC', 'BCHABCTUSD', 'BCHABCPAX', 'BCHABCUSDC', 'BCHSVTUSD', 'BCHSVPAX', 'BCHSVUSDC', 'LTCTUSD', 'LTCPAX', 'LTCUSDC', 'TRXPAX', 'TRXUSDC', 'BTTBTC', 'BTTBNB', 'BTTUSDT', 'BNBUSDS', 'BTCUSDS', 'USDSUSDT', 'USDSPAX', 'USDSTUSD', 'USDSUSDC', 'BTTPAX', 'BTTTUSD', 'BTTUSDC', 'ONGBNB', 'ONGBTC', 'ONGUSDT', 'HOTBNB', 'HOTUSDT', 'ZILUSDT', 'ZRXBNB', 'ZRXUSDT', 'FETBNB', 
'FETBTC', 'FETUSDT', 'BATUSDT', 'XMRBNB', 'XMRUSDT', 'ZECBNB', 'ZECUSDT', 'ZECPAX', 'ZECTUSD', 'ZECUSDC', 'IOSTBNB', 'IOSTUSDT', 'CELRBNB', 'CELRBTC', 'CELRUSDT', 'ADAPAX', 'ADAUSDC', 'NEOPAX', 'NEOUSDC', 'DASHBNB', 'DASHUSDT', 'NANOUSDT', 'OMGBNB', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICBNB', 'MATICBTC', 'MATICUSDT', 'ATOMBNB', 'ATOMBTC', 'ATOMUSDT', 'ATOMUSDC', 'ATOMPAX', 'ATOMTUSD', 'ETCUSDC', 'ETCPAX', 'ETCTUSD', 'BATUSDC', 'BATPAX', 'BATTUSD', 'PHBBNB', 'PHBBTC', 'PHBUSDC', 'PHBTUSD', 
'PHBPAX', 'TFUELBNB', 'TFUELBTC', 'TFUELUSDT', 'TFUELUSDC', 'TFUELTUSD', 'TFUELPAX', 'ONEBNB', 'ONEBTC', 'ONEUSDT', 'ONETUSD', 'ONEPAX', 'ONEUSDC', 'FTMBNB', 'FTMBTC', 'FTMUSDT', 'FTMTUSD', 'FTMPAX', 'FTMUSDC', 'BTCBBTC', 'BCPTTUSD', 'BCPTPAX', 'BCPTUSDC', 'ALGOBNB', 'ALGOBTC', 'ALGOUSDT', 'ALGOTUSD', 'ALGOPAX', 'ALGOUSDC', 'USDSBUSDT', 'USDSBUSDS', 'GTOUSDT', 'GTOPAX', 'GTOTUSD', 'GTOUSDC', 'ERDBNB', 'ERDBTC', 'ERDUSDT', 'ERDPAX', 'ERDUSDC', 'DOGEBNB', 'DOGEBTC', 'DOGEUSDT', 'DOGEPAX', 'DOGEUSDC', 
'DUSKBNB', 'DUSKBTC', 'DUSKUSDT', 'DUSKUSDC', 'DUSKPAX', 'BGBPUSDC', 'ANKRBNB', 'ANKRBTC', 'ANKRUSDT', 'ANKRTUSD', 'ANKRPAX', 'ANKRUSDC', 'ONTPAX', 'ONTUSDC', 'WINBNB', 'WINBTC', 'WINUSDT', 'WINUSDC', 'COSBNB', 'COSBTC', 'COSUSDT', 'TUSDBTUSD', 'NPXSUSDT', 'NPXSUSDC', 'COCOSBNB', 'COCOSBTC', 'COCOSUSDT', 'MTLUSDT', 'TOMOBNB', 'TOMOBTC', 'TOMOUSDT', 'TOMOUSDC', 'PERLBNB', 'PERLBTC', 'PERLUSDC', 'PERLUSDT', 'DENTUSDT', 'MFTUSDT', 'KEYUSDT', 'STORMUSDT', 'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'BTTTRX', 
'WINTRX', 'CHZBNB', 'CHZBTC', 'CHZUSDT', 'BANDBNB', 'BANDBTC', 'BANDUSDT', 'BNBBUSD', 'BTCBUSD', 'BUSDUSDT', 'BEAMBNB', 'BEAMBTC', 'BEAMUSDT', 'XTZBNB', 'XTZBTC', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HCUSDT', 'HBARBNB', 'HBARBTC', 'HBARUSDT', 'NKNBNB', 'NKNBTC', 'NKNUSDT', 'XRPBUSD', 'ETHBUSD', 'BCHABCBUSD', 'LTCBUSD', 'LINKBUSD', 'ETCBUSD', 'STXBNB', 'STXBTC', 'STXUSDT', 'KAVABNB', 'KAVABTC', 'KAVAUSDT', 'BUSDNGN', 'BNBNGN', 'BTCNGN', 'ARPABNB', 'ARPABTC', 'ARPAUSDT', 'TRXBUSD', 'EOSBUSD', 'IOTXUSDT', 'RLCUSDT', 
'MCOUSDT', 'XLMBUSD', 'ADABUSD', 'CTXCBNB', 'CTXCBTC', 'CTXCUSDT', 'BCHBNB', 'BCHBTC', 'BCHUSDT', 'BCHUSDC', 'BCHTUSD', 'BCHPAX', 'BCHBUSD', 'BTCRUB', 'ETHRUB', 'XRPRUB', 'BNBRUB', 'TROYBNB', 'TROYBTC', 'TROYUSDT', 'BUSDRUB', 'QTUMBUSD', 'VETBUSD', 'VITEBNB', 'VITEBTC', 'VITEUSDT', 'FTTBNB', 'FTTBTC', 'FTTUSDT', 'BTCTRY', 'BNBTRY', 'BUSDTRY', 'ETHTRY', 'XRPTRY', 'USDTTRY', 'USDTRUB', 'BTCEUR', 'ETHEUR', 'BNBEUR', 'XRPEUR', 'EURBUSD', 'EURUSDT', 'OGNBNB', 'OGNBTC', 'OGNUSDT', 'DREPBNB', 'DREPBTC', 'DREPUSDT', 
'BULLUSDT', 'BULLBUSD', 'BEARUSDT', 'BEARBUSD', 'ETHBULLUSDT', 'ETHBULLBUSD', 'ETHBEARUSDT', 'ETHBEARBUSD', 'TCTBNB', 'TCTBTC', 'TCTUSDT', 'WRXBNB', 'WRXBTC', 'WRXUSDT', 'ICXBUSD', 'BTSUSDT', 'BTSBUSD', 'LSKUSDT', 'BNTUSDT', 'BNTBUSD', 'LTOBNB', 'LTOBTC', 'LTOUSDT', 'ATOMBUSD', 'DASHBUSD', 'NEOBUSD', 'WAVESBUSD', 'XTZBUSD', 'EOSBULLUSDT', 'EOSBULLBUSD', 'EOSBEARUSDT', 'EOSBEARBUSD', 'XRPBULLUSDT', 'XRPBULLBUSD', 'XRPBEARUSDT', 'XRPBEARBUSD', 'BATBUSD', 'ENJBUSD', 'NANOBUSD', 'ONTBUSD', 'RVNBUSD', 'STRATBUSD', 
'STRATBNB', 'STRATUSDT', 'AIONBUSD', 'AIONUSDT', 'MBLBNB', 'MBLBTC', 'MBLUSDT', 'COTIBNB', 'COTIBTC', 'COTIUSDT', 'ALGOBUSD', 'BTTBUSD', 'TOMOBUSD', 'XMRBUSD', 'ZECBUSD', 'BNBBULLUSDT', 'BNBBULLBUSD', 'BNBBEARUSDT', 'BNBBEARBUSD', 'STPTBNB', 'STPTBTC', 'STPTUSDT', 'BTCZAR', 'ETHZAR', 'BNBZAR', 'USDTZAR', 'BUSDZAR', 'BTCBKRW', 'ETHBKRW', 'BNBBKRW', 'WTCUSDT', 'DATABUSD', 'DATAUSDT', 'XZCUSDT', 'SOLBNB', 'SOLBTC', 'SOLUSDT', 'SOLBUSD', 'BTCIDRT', 'BNBIDRT', 'USDTIDRT', 'BUSDIDRT', 'CTSIBTC', 'CTSIUSDT', 'CTSIBNB', 
'CTSIBUSD', 'HIVEBNB', 'HIVEBTC', 'HIVEUSDT', 'CHRBNB', 'CHRBTC', 'CHRUSDT', 'BTCUPUSDT', 'BTCDOWNUSDT', 'GXSUSDT', 'ARDRUSDT', 'ERDBUSD', 'LENDUSDT', 'HBARBUSD', 'MATICBUSD', 'WRXBUSD', 'ZILBUSD', 'MDTBNB', 'MDTBTC', 'MDTUSDT', 'STMXBNB', 'STMXBTC', 'STMXETH', 'STMXUSDT', 'KNCBUSD', 'KNCUSDT', 'REPBUSD', 'REPUSDT', 'LRCBUSD', 'LRCUSDT', 'IQBNB', 'IQBUSD', 'PNTBTC', 'PNTUSDT', 'BTCGBP', 'ETHGBP', 'XRPGBP', 'BNBGBP', 'GBPBUSD', 'DGBBNB', 'DGBBTC', 'DGBBUSD', 'BTCUAH', 'USDTUAH', 'COMPBTC', 'COMPBNB', 'COMPBUSD', 
'COMPUSDT', 'BTCBIDR', 'ETHBIDR', 'BNBBIDR', 'BUSDBIDR', 'USDTBIDR', 'BKRWUSDT', 'BKRWBUSD', 'SCUSDT', 'ZENUSDT', 'SXPBTC', 'SXPBNB', 'SXPBUSD', 'SNXBTC', 'SNXBNB', 'SNXBUSD', 'SNXUSDT', 'ETHUPUSDT', 'ETHDOWNUSDT', 'ADAUPUSDT', 'ADADOWNUSDT', 'LINKUPUSDT', 'LINKDOWNUSDT', 'VTHOBNB', 'VTHOBUSD', 'VTHOUSDT', 'DCRBUSD', 'DGBUSDT', 'GBPUSDT', 'STORJBUSD', 'SXPUSDT', 'IRISBNB', 'IRISBTC', 'IRISBUSD', 'MKRBNB', 'MKRBTC', 'MKRUSDT', 'MKRBUSD', 'DAIBNB', 'DAIBTC', 'DAIUSDT', 'DAIBUSD', 'RUNEBNB', 'RUNEBTC', 'RUNEBUSD', 
'MANABUSD', 'DOGEBUSD', 'LENDBUSD', 'ZRXBUSD', 'DCRUSDT', 'STORJUSDT', 'XRPBKRW', 'ADABKRW', 'BTCAUD', 'ETHAUD', 'AUDBUSD', 'FIOBNB', 'FIOBTC', 'FIOBUSD', 'BNBUPUSDT', 'BNBDOWNUSDT', 'XTZUPUSDT', 'XTZDOWNUSDT', 'AVABNB', 'AVABTC', 'AVABUSD', 'USDTBKRW', 'BUSDBKRW', 'IOTABUSD', 'MANAUSDT', 'XRPAUD', 'BNBAUD', 'AUDUSDT', 'BALBNB', 'BALBTC', 'BALBUSD', 'YFIBNB', 'YFIBTC', 'YFIBUSD', 'YFIUSDT', 'BLZBUSD', 'KMDBUSD', 'BALUSDT', 'BLZUSDT', 'IRISUSDT', 'KMDUSDT', 'BTCDAI', 'ETHDAI', 'BNBDAI', 'USDTDAI', 'BUSDDAI', 
'JSTBNB', 'JSTBTC', 'JSTBUSD', 'JSTUSDT', 'SRMBNB', 'SRMBTC', 'SRMBUSD', 'SRMUSDT', 'ANTBNB', 'ANTBTC', 'ANTBUSD', 'ANTUSDT', 'CRVBNB', 'CRVBTC', 'CRVBUSD', 'CRVUSDT', 'SANDBNB', 'SANDBTC', 'SANDUSDT', 'SANDBUSD', 'OCEANBNB', 'OCEANBTC', 'OCEANBUSD', 'OCEANUSDT', 'NMRBNB', 'NMRBTC', 'NMRBUSD', 'NMRUSDT', 'DOTBNB', 'DOTBTC', 'DOTBUSD', 'DOTUSDT', 'LUNABNB', 'LUNABTC', 'LUNABUSD', 'LUNAUSDT', 'IDEXBTC', 'IDEXBUSD', 'RSRBNB', 'RSRBTC', 'RSRBUSD', 'RSRUSDT', 'PAXGBNB', 'PAXGBTC', 'PAXGBUSD', 'PAXGUSDT', 'WNXMBNB', 
'WNXMBTC', 'WNXMBUSD', 'WNXMUSDT', 'TRBBNB', 'TRBBTC', 'TRBBUSD', 'TRBUSDT', 'ETHNGN', 'DOTBIDR', 'LINKAUD', 'SXPAUD', 'BZRXBNB', 'BZRXBTC', 'BZRXBUSD', 'BZRXUSDT', 'WBTCBTC', 'WBTCETH', 'SUSHIBNB', 'SUSHIBTC', 'SUSHIBUSD', 'SUSHIUSDT', 'YFIIBNB', 'YFIIBTC', 'YFIIBUSD', 'YFIIUSDT', 'KSMBNB', 'KSMBTC', 'KSMBUSD', 'KSMUSDT', 'EGLDBNB', 'EGLDBTC', 'EGLDBUSD', 'EGLDUSDT', 'DIABNB', 'DIABTC', 'DIABUSD', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMABTC', 'UMAUSDT', 'EOSUPUSDT', 'EOSDOWNUSDT', 'TRXUPUSDT', 'TRXDOWNUSDT', 
'XRPUPUSDT', 'XRPDOWNUSDT', 'DOTUPUSDT', 'DOTDOWNUSDT', 'SRMBIDR', 'ONEBIDR', 'LINKTRY', 'USDTNGN', 'BELBNB', 'BELBTC', 'BELBUSD', 'BELUSDT', 'WINGBNB', 'WINGBTC', 'SWRVBNB', 'SWRVBUSD', 'WINGBUSD', 'WINGUSDT', 'LTCUPUSDT', 'LTCDOWNUSDT', 'LENDBKRW', 'SXPEUR', 'CREAMBNB', 'CREAMBUSD', 'UNIBNB', 'UNIBTC', 'UNIBUSD', 'UNIUSDT', 'NBSBTC', 'NBSUSDT', 'OXTBTC', 'OXTUSDT', 'SUNBTC', 'SUNUSDT', 'AVAXBNB', 'AVAXBTC', 'AVAXBUSD', 'AVAXUSDT', 'HNTBTC', 'HNTUSDT', 'BAKEBNB', 'BURGERBNB', 'SXPBIDR', 'LINKBKRW', 'FLMBNB', 
'FLMBTC', 'FLMBUSD', 'FLMUSDT', 'SCRTBTC', 'SCRTETH', 'CAKEBNB', 'CAKEBUSD', 'SPARTABNB', 'UNIUPUSDT', 'UNIDOWNUSDT', 'ORNBTC', 'ORNUSDT', 'TRXNGN', 'SXPTRY', 'UTKBTC', 'UTKUSDT', 'XVSBNB', 'XVSBTC', 'XVSBUSD', 'XVSUSDT', 'ALPHABNB', 'ALPHABTC', 'ALPHABUSD', 'ALPHAUSDT', 'VIDTBTC', 'VIDTBUSD', 'AAVEBNB', 'BTCBRL', 'USDTBRL', 'AAVEBTC', 'AAVEETH', 'AAVEBUSD', 'AAVEUSDT', 'AAVEBKRW', 'NEARBNB', 'NEARBTC', 'NEARBUSD', 'NEARUSDT', 'SXPUPUSDT', 'SXPDOWNUSDT', 'DOTBKRW', 'SXPGBP', 'FILBNB', 'FILBTC', 'FILBUSD', 
'FILUSDT', 'FILUPUSDT', 'FILDOWNUSDT', 'YFIUPUSDT', 'YFIDOWNUSDT', 'INJBNB', 'INJBTC', 'INJBUSD', 'INJUSDT', 'AERGOBTC', 'AERGOBUSD', 'LINKEUR', 'ONEBUSD', 'EASYETH', 'AUDIOBTC', 'AUDIOBUSD', 'AUDIOUSDT', 'CTKBNB', 'CTKBTC', 'CTKBUSD', 'CTKUSDT', 'BCHUPUSDT', 'BCHDOWNUSDT', 'BOTBTC', 'BOTBUSD', 'ETHBRL', 'DOTEUR', 'AKROBTC', 'AKROUSDT', 'KP3RBNB', 'KP3RBUSD', 'AXSBNB', 'AXSBTC', 'AXSBUSD', 'AXSUSDT', 'HARDBNB', 'HARDBTC', 'HARDBUSD', 'HARDUSDT', 'BNBBRL', 'LTCEUR', 'RENBTCBTC', 'RENBTCETH', 'DNTBUSD', 'DNTUSDT', 'SLPETH', 'ADAEUR', 'LTCNGN']

#Groups of three pairs used in each triangular arbitrage
triangles = [
    ['NEOUSDT', 'NEOUSDC', 'USDCUSDT'], 
    ['LTCUSDT', 'LTCBUSD', 'BUSDUSDT'], 
    ['BTCUSDT', 'QTUMBTC', 'QTUMUSDT'],
    ['NEOUSDT', 'NEOBNB', 'BNBUSDT']
]

#Other currencies that will be formatted into triangles | Not being used in the program currently
others = [ 
    ['ADABTC', 'ADAETH', 'ADABNB', 'ADAEUR', 'ADAUSDT', 'ADAPAX', 'ADABUSD', 'ADAUSDC', 'ADAUPUSDT', 'ADABKRW', 'ADATUSD'], 
    ['XZCXRP', 'XRPTRY', 'TRXXRP', 'XRPBKRW', 'XRPBUSD', 'XRPBTC', 'XRPUSDT', 'XRPBNB', 'XRPUSDC', 'XRPGBP', 'XRPPAX', 'XRPAUD', 'XRPETH', 'XRPRUB', 'XRPEUR'], 
    ['EOSBUSD', 'EOSBNB', 'EOSETH', 'EOSBTC', 'EOSUSDC', 'EOSPAX', 'EOSUSDT', 'EOSTUSD'], 
    ['IOTAUSDT', 'IOTABUSD', 'IOTABTC', 'IOTABNB', 'IOTAETH'], 
    ['XLMUSDC', 'XLMTUSD', 'XLMBUSD', 'XLMPAX', 'XLMETH', 'XLMBNB', 'XLMBTC', 'XLMUSDT'], 
    ['ONTBTC', 'ONTPAX', 'ONTUSDC', 'ONTBNB', 'ONTETH', 'ONTBUSD', 'ONTUSDT'], 
    ['TRXNGN', 'TRXTUSD', 'TRXUSDT', 'TRXETH', 'TRXPAX', 'TRXBNB', 'TRXXRP', 'TRXBUSD', 'TRXBTC', 'TRXUSDC', 'BTTTRX', 'WINTRX'], 
    ['ETCETH', 'ETCBNB', 'ETCUSDC', 'ETCTUSD', 'ETCBTC', 'ETCPAX', 'ETCBUSD', 'ETCUSDT'], 
    ['ICXBTC', 'ICXBNB', 'ICXUSDT', 'ICXETH', 'ICXBUSD'], 
    ['VENETH', 'VENBNB', 'VENBTC', 'VENUSDT'], 
    ['NULSUSDT', 'NULSBTC', 'NULSETH', 'NULSBNB'], 
    ['VETBNB', 'VETBTC', 'VETBUSD', 'VETETH', 'NAVETH', 'VETUSDT'], 
    ['BCHABCBUSD', 'BCHABCTUSD', 'BCHABCPAX', 'BCHABCUSDT', 'BCHABCUSDC', 'BCHABCBTC'], 
    ['BCHSVUSDT', 'BCHSVBTC', 'BCHSVTUSD', 'BCHSVPAX', 'BCHSVUSDC'], 
    ['LINKUSDT', 'LINKTUSD', 'LINKBTC', 'LINKBUSD', 'LINKUSDC', 'LINKEUR', 'LINKBKRW', 'LINKETH', 'LINKTRY', 'LINKPAX', 'LINKAUD'], 
    ['WAVESUSDT', 'WAVESPAX', 'WAVESBTC', 'WAVESUSDC', 'WAVESETH', 'WAVESBNB', 'WAVESTUSD', 'WAVESBUSD'], 
    ['BTTUSDC', 'BTTBUSD', 'BTTBTC', 'BTTUSDT', 'BTTBNB', 'BTTTRX', 'BTTTUSD', 'BTTPAX'], 
    ['USDSPAX', 'USDSTUSD', 'USDSUSDT', 'USDSUSDC', 'USDSBUSDS', 'USDSBUSDT', 'BTCUSDS', 'BNBUSDS'], 
    ['ONGBNB', 'ONGBTC', 'ONGUSDT'], 
    ['HOTBNB', 'HOTBTC', 'HOTETH', 'HOTUSDT'], 
    ['ZILBTC', 'ZILBNB', 'ZILETH', 'ZILBUSD', 'ZILUSDT'], 
    ['ZRXBUSD', 'ZRXBNB', 'ZRXUSDT', 'ZRXBTC', 'ZRXETH'], 
    ['FETBTC', 'FETUSDT', 'FETBNB'], 
    ['DNTUSDT', 'DNTBTC', 'DNTETH', 'DNTBUSD'], 
    ['HARDBNB', 'HARDBUSD', 'HARDUSDT', 'HARDBTC'], 
    ['AXSUSDT', 'AXSBTC', 'AXSBUSD', 'AXSBNB'], 
    ['CTKBNB', 'CTKBUSD', 'CTKBTC', 'CTKUSDT'], 
    ['AUDIOUSDT', 'AUDIOBTC', 'AUDIOBUSD'], 
    ['INJBNB', 'INJBUSD', 'INJBTC', 'INJUSDT'], 
    ['NEARBUSD', 'NEARUSDT', 'NEARBNB', 'NEARBTC'], 
    ['AAVEETH', 'AAVEBKRW', 'AAVEBNB', 'AAVEBTC', 'AAVEBUSD', 'AAVEUSDT'], 
    ['XVSUSDT', 'XVSBUSD', 'XVSBTC', 'XVSBNB'], 
    ['AVAXBTC', 'AVAXUSDT', 'AVAXBUSD', 'AVAXBNB'], 
    ['BELBNB', 'BELBTC', 'BELBUSD', 'BELUSDT'], 
    ['FIOBTC', 'FIOUSDT', 'FIOBUSD', 'FIOBNB'], 
    ['RUNEBNB', 'RUNEBTC', 'RUNEBUSD', 'RUNEUSDT'], 
    ['DIABUSD', 'DIABTC', 'DIABNB', 'DIAUSDT'], 
    ['EGLDBNB', 'EGLDUSDT', 'EGLDBTC', 'EGLDBUSD'], 
    ['KSMBUSD', 'KSMBNB', 'KSMUSDT', 'KSMBTC'], 
    ['YFIIBTC', 'YFIIBNB', 'YFIIUSDT', 'YFIIBUSD'], 
    ['SUSHIBTC', 'SUSHIBUSD', 'SUSHIUSDT', 'SUSHIBNB']
]

def stripf(word, term):
    return word.replace(term, "")

#Returns if whether each pair needs to be bought or sold in triangular arbitrage transaction
def sides(pairs):
    strip = lambda x: x.replace("USDT", "")
    if pairs[0][-4:] == 'USDT':
        first = "BUY"
    else:
        first = False
    if strip(pairs[0]) == pairs[1][:-len(strip(pairs[0]))]:
        second = "SELL"
    else:
        second = "BUY"
    if "USDT" == pairs[2][-4:]:
        third = "SELL"
    else:
        third = "BUY"
    return first, second, third

#The number of decimals a pair allows for its price when making an order
def get_precision(pairs):
    precisions = []
    info = requests.get("https://www.binance.com/api/v1/exchangeInfo").json()
    for pair in pairs:
        i = PAIRS.index(pair)
        ticksize = info["symbols"][i]["filters"][0]['tickSize']
        precision = abs(round(math.log(float(ticksize), 10)))
        precisions.append(precision)
    return precisions

#Prices of each of the three pairs in the triangular arbitrage transaction
def triangle(pairs):
    strip = lambda x: x.replace("USDT", "")
    if pairs[0][-4:] == 'USDT':
        first = float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pairs[0]}").json()['price'])
    else:
        first = 1/float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pairs[0]}").json()['price'])
    if strip(pairs[0]) == pairs[1][:-len(strip(pairs[0]))]:
        second = 1/float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pairs[1]}").json()['price'])
    else:
        second = float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pairs[1]}").json()['price'])
    if pairs[2][:4] == "USDT":
        third = float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pairs[2]}").json()['price'])
    else:
        third = 1/float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={pairs[2]}").json()['price'])
    return first, second, third

#Loop printing if the three pairs are above a certain margin
#Will add order functions to enact transaction if it is above the margin
def enact(input, pairs, margin=0):
    precisions = get_precision(pairs)
    s = sides(pairs)
    while True:
        rates = triangle(pairs)
        one = round_down(rates[0], precisions[0])
        two = round_down(rates[1], precisions[1])
        three = round_down(rates[2], precisions[2])
        if input*rates[0]*FEE*rates[1]*FEE*rates[2]*FEE >= input * margin:
            print(input*one*two*three)
            #Insert order functions here
        time.sleep(0.5)
        if KeyboardInterrupt:
            break

def main():
    input = 50
    for item in triangles:
        threadobj = threading.Thread(target=enact, args=[input, item])
        threadobj.start()

if __name__ == '__main__':
    main()