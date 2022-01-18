
import requests, json
params={}
r = requests.get('https://api.opensea.io/api/v1/events', params=params)
print(r)

import requests

url = "https://api.opensea.io/api/v1/events?only_opensea=false&offset=0&limit=20"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "a156e53acdfc46e09f5ba654af640f50"
}

response = requests.request("GET", url, headers=headers)

print(response.text)