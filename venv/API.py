import requests
import sys

r = requests.get('https://api.blockchain.info/stats')
lalo = r.json()

mostrar = (sys.argv[1])

market_price = lalo['market_price_usd']
total_bc = lalo['totalbc']


#print(total_bc)
#print(market_price)

if mostrar == 'market_price':
    print(total_bc * market_price)

elif mostrar == 'totalbc':
    print(total_bc)






#print("Número de parámetros: ", len(sys.argv))
#print("Lista de argumentos: ", sys.argv)



"""if (sys.argv[1]) == 'market_price_usd':
    texto = sys.argv[1]
    print(texto)

elif (sys.argv[2]) == 'totalbc':
    texto = sys.argv[2]
    print(texto)"""