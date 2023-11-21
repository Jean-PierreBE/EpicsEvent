import requests
import json
from .constants import URL, LOGIN
from http.client import responses

def login(user, password):
    params = {
        "pseudo": "",
        "password": ""
    }
    params["pseudo"] = user
    params["password"] = password

    r = requests.post(URL + LOGIN, json=params)

    if r.status_code == 200:
        json_ret = r.json()
        print(json_ret)
        return 0, responses[r.status_code], json_ret['access']
    else:
        return 1, responses[r.status_code], ''

def signup(token):
    params = {
        "pseudo": "jps10",
        "first_name": "jean",
        "last_name": "pierre",
        "email": "jps10@mail.be",
        "role": "COM",
        "password": "Ulysse1786"
        }
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    print(token)
    r = requests.post(URL + LOGIN, json=params, headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return 0
    else:
        return 1
