import requests
from http.client import responses
from .constants import END_POINT


def login(user, password):
    params = {
        "pseudo": "",
        "password": ""
    }
    params["pseudo"] = user
    params["password"] = password

    ret_code = requests.post(END_POINT["URL"] + END_POINT["LOGIN"], json=params)

    if ret_code.status_code == 200:
        json_ret = ret_code.json()
        return 0, responses[ret_code.status_code], json_ret['access'], json_ret['refresh']
    else:
        return 1, responses[ret_code.status_code], '', ''
