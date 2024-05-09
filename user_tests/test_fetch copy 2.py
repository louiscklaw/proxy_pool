from pprint import pprint
from time import sleep

import requests

url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'

r = requests.get(url)
for i in r.text.split('\n'):
    yield i

# for i in range(0,len(r.text()['data'])):
#     ip = r.text()['data'][i]['ip']
#     port = r.text()['data'][i]['port']
#     print(ip+":"+port)

