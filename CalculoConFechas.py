import requests, sys
import json
from pylab import *

fecha1 = (sys.argv[1])
fecha2 = (sys.argv[2])

r = requests.get(f'https://api.coindesk.com/v1/bpi/historical/close.json?start={fecha1}&end={fecha2}')
infoPag = r.json()
infoPag = infoPag['bpi']

dates = list(infoPag.keys()) #string
mount = list(infoPag.values()) #double


def calculo_ganancia(market_price, date):
    cant_a_comprar = int(sys.argv[3])
    print(f'{(((market_price * cant_a_comprar) * 100) / 3)} : {date}')

for x in dates:
    calculo_ganancia(infoPag.get(x),x)

