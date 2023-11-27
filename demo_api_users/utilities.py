import requests
import json
from constants import END_POINT
from http.client import responses

def signup(token, pseudo, first_name, last_name, email, role, password):
    print("02 " + token)
    params = {
        "pseudo": pseudo,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "role": role,
        "password": password
        }
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.post(END_POINT["URL"] + END_POINT["SIGNUP"], json=params, headers=headers)
    print(r.status_code)
    if r.status_code == 200:
        return 0
    else:
        return 1
