import matplotlib.pyplot as plt
import requests, sys
import json
from pylab import *

fecha1 = (sys.argv[1])
fecha2 = (sys.argv[2])

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

