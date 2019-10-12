import requests

url = 'http://localhost:5000/mine'
payload = {}
result = requests.get(url, params=payload)
print(result.json())