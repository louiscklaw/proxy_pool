from pprint import pprint
from time import sleep

import requests

urls = [
    'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
    'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
]

for url in urls:
    r = requests.get(url)
    for i in r.text.split('\n'):
        try:
            print(i.split(':')[0]+":"+i.split(':')[1])

        except Exception as e:
            print(i)
    

# for i in range(0,len(r.text()['data'])):
#     ip = r.text()['data'][i]['ip']
#     port = r.text()['data'][i]['port']
#     print(ip+":"+port)

