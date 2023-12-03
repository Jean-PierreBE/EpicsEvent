import requests
from http.client import responses
from constants import END_POINT
def login(user, password):
    params = {
        "pseudo": "",
        "password": ""
    }
    params["pseudo"] = user
    params["password"] = password

    r = requests.post(END_POINT["URL"] + END_POINT["LOGIN"], json=params)

    if r.status_code == 200:
        json_ret = r.json()
        return 0, responses[r.status_code], json_ret['access'], json_ret['refresh']
    else:
        return 1, responses[r.status_code], '', ''
