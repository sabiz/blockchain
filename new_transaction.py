import requests
import json

url = 'http://localhost:5000/transactions/new'
payload = {
    "sender": "1",
    "recipient": "ea945207f9d2415591028192ea3e0339",
    "amount": 1,
}
result = requests.post(url, json.dumps(payload), headers={'Content-Type': 'application/json'})
print(result.json())