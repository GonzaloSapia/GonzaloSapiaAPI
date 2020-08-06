import requests
import sys

r = requests.get('https://api.blockchain.info/stats')
infoPag = r.json()   #esto me trae la data del URL

mostrar = (sys.argv[1])
cant_a_comprar = int(sys.argv[2])
porc_gan = int(sys.argv[3])



market_price = infoPag['market_price_usd']
total_bc = infoPag['totalbc']



if mostrar == 'market_price':
    print(market_price)

elif mostrar == 'calcu_ganancia':
    print(((market_price * cant_a_comprar) * 100) / porc_gan)

else:
    print(total_bc)



#  print(((market_price * cant_a_comprar) * 100) / porc_gan)):



#print(total_bc)
#print(market_price)



#pasar el monto de bitcoins, y el porcentaje de ganancia que voy a tener por comprar/vender el bc. Pasar por parametro cuantos bc voy a comprar y cual va a ser mi porcentaje de ganancia.




#print("Número de parámetros: ", len(sys.argv))
#print("Lista de argumentos: ", sys.argv)
