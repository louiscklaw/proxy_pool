import requests

# Define the URL you want to request
url = 'http://carousell.com.hk'

# Set up the proxies dictionary. Proxies are typically provided in the format 'protocol://host:port'.
# For example: 'http://192.168.1.1:8080'
proxies = {
    'http': 'http://47.56.110.204:8989',
}

# Make a GET request through the proxy
response = requests.get(url, proxies=proxies)

# Print the status code and content of the response
print(response.status_code)
print(response.text)