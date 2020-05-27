import requests
import json

api_endpoint_url = 'http://staging-live.idchronos.it/api/secured-endpoint'

auth_token = ''

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + auth_token,
}

r = requests.get(api_endpoint_url,headers=headers)

print(r.text)
