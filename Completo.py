import requests
import sys
import json
from pylab import *
from argparse import ArgumentParser



r = requests.get('https://api.blockchain.info/stats')
infoPag = r.json()   #esto me trae la data del URL

mostrar = (sys.argv[1])

market_price = infoPag['market_price_usd']
total_bc = infoPag['totalbc']


def precio_de_mercado():
    print(market_price * total_bc)


def ganancia_por_btc():
    porc_gan = int(sys.argv[2])
    print((market_price * 100) / porc_gan)

def grafico():
    fecha1 = (sys.argv[2])
    fecha2 = (sys.argv[3])

    r = requests.get(f'https://api.coindesk.com/v1/bpi/historical/close.json?start={fecha1}&end={fecha2}')
    infoPag = r.json()

    dates = list(infoPag['bpi'].keys())
    mount = list(infoPag['bpi'].values())

    figure()
    plot(dates, mount, 'r')
    xlabel('dates')
    ylabel('mount')
    title('btc')
    plt.show()

def calc_gan_sin_porc(): #PRECIO DEL BTC HOY
    cant_a_comprar = int(sys.argv[2])
    porc_gan = int(sys.argv[3])
    print(((market_price * cant_a_comprar) * 100) / porc_gan)

def calc_gan_con_porc(market_price, date):
    fecha1 = (sys.argv[2])
    fecha2 = (sys.argv[3])

    r = requests.get(f'https://api.coindesk.com/v1/bpi/historical/close.json?start={fecha1}&end={fecha2}')
    infoPag = r.json()
    infoPag = infoPag['bpi']

    dates = list(infoPag.keys())  # string
    mount = list(infoPag.values())  # double


    cant_a_comprar = int(sys.argv[3])
    print(f'{(((market_price * cant_a_comprar) * 100) / 3)} : {date}')

    for x in dates:
        calc_gan_con_porc(infoPag.get(x), x)

p = ArgumentParser (description= 'Elegi la cuenta que queres realizar')





"""if (mostrar == 'market_price'):
    precio_de_mercado()
elif(mostrar == 'calc_gan_sin'):
    calc_gan_sin_porc()
elif(grafico == 'grafico'):
    grafico()
elif(mostrar == 'gan_por_btc'):
    ganancia_por_btc()
elif(mostrar == 'gan_por_btc'):
    ganancia_por_btc()"""


