import requests as req

headers = {
    'X-Username': 'chief.engineer',
    'X-Password': 'ares-vallis-7'
}

response = req.get('http://20.127.202.175:8000', headers=headers)

print(response.text)