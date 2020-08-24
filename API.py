import requests
import sys, argparse


r = requests.get('https://api.blockchain.info/stats')
infoPag = r.json()   #esto me trae la data del URL

mostrar = (sys.argv[1])

market_price = infoPag['market_price_usd']
total_bc = infoPag['totalbc']


def precio_de_mercado():
    print(market_price * total_bc)

def calculo_ganancia():
    cant_a_comprar = int(sys.argv[2])
    porc_gan = int(sys.argv[3])
    print(((market_price * cant_a_comprar) * 100) / porc_gan)

def calcu_multiplicacion():
    cant_a_comprar = int(sys.argv[2])
    print(market_price * cant_a_comprar)

def ganancia_por_btc():
    porc_gan = int(sys.argv[2])
    print((market_price * 100) / porc_gan)


if (mostrar == 'market_price'):
    precio_de_mercado()
elif(mostrar == 'calcu_ganancia'):
    calculo_ganancia()
elif(mostrar == 'calcu_multi'):
    calcu_multiplicacion()
elif(mostar == 'gan_por_btc'):
    ganancia_por_btc()
