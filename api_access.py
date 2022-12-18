import requests, json


URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(URL)
data = json.loads(response.content.decode('utf-8'))
print(data)

bitcoin_price = data['bpi']['USD']['rate_float']
print(bitcoin_price)
