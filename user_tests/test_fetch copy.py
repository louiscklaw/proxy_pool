from pprint import pprint
from time import sleep

import requests

url = 'https://proxylist.geonode.com/api/proxy-list?protocols=http%2Chttps&limit=500&page=1'

r = requests.get(url)

for i in range(0,len(r.json()['data'])):
    ip = r.json()['data'][i]['ip']
    port = r.json()['data'][i]['port']
    print(ip+":"+port)

