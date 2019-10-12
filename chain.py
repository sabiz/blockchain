import requests

url = 'http://localhost:5000/chain'
payload = {}
result = requests.get(url, params=payload)
print(result.json())