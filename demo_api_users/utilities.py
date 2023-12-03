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
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["SIGNUP"] + str(user_id), headers=headers).json()
    print(r)
    params = {}
    if pseudo == "blank":
        params["pseudo"] = r["pseudo"]
    else:
        params["pseudo"] = pseudo
    if first_name == "blank":
        params["first_name"] = r["first_name"]
    else:
        params["first_name"] = first_name
    if last_name == "blank":
        params["last_name"] = r["last_name"]
    else:
        params["last_name"] = last_name
    if email == "blank":
        params["email"] = r["email"]
    else:
        params["email"] = email
    if role == "blank":
        params["role"] = r["role"]
    else:
        params["role"] = role
    params["password"] = password
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["SIGNUP"] + str(user_id) + "/", json=params, headers=headers)
    return r.status_code, r.content

def signup_all(token):
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["SIGNUP"], headers=headers)
    return r.status_code, r.content

def signup_one(token, user_id):
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["SIGNUP"] + str(user_id), headers=headers)
    return r.status_code, r.content

def refresh(token):
    params = {
        "refresh": token
    }
    r = requests.post(END_POINT["URL"] + END_POINT["REFRESH"], data=params)
    return r.status_code, r.content
