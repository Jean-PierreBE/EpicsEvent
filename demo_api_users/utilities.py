import requests
import json
from constants import END_POINT
from http.client import responses

def signup(token, pseudo, first_name, last_name, email, role, password):
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
    return r.status_code, r.content

def delete(token, user_id):
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.delete(END_POINT["URL"] + END_POINT["SIGNUP"] + str(user_id), headers=headers)
    return r.status_code, r.content

def update(token, user_id, pseudo, first_name, last_name, email, role, password):
    params = {
        "pseudo": pseudo,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "role": role,
        "password": password
    }
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["SIGNUP"] + str(user_id) + "/", json=params, headers=headers)
    return r.status_code, r.content
