import requests
from constants import END_POINT


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
    print("delete(token, user_id) ")
    r = requests.delete(END_POINT["URL"] + END_POINT["SIGNUP"] + str(user_id) + "/", headers=headers)
    print("r.status_code " + str(r.status_code))
    return r.status_code, r.content

def update(token, user_id, pseudo, first_name, last_name, email, role, password):
    params["pseudo"] = pseudo
    params["first_name"] = first_name
    params["last_name"] = last_name
    params["email"] = email
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
