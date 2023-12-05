import requests
from demo_api.constants import END_POINT

def create_event(token, enterprise_name, client_name , information ,email, phone):
    params = {
        "enterprise_name": enterprise_name,
        "client_name": client_name,
        "information": information,
        "email": email,
        "phone": phone
        }
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.post(END_POINT["URL"] + END_POINT["EVENT"], json=params, headers=headers)
    return r.status_code, r.content

def delete_event(token, event_id):
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.delete(END_POINT["URL"] + END_POINT["EVENT"] + str(event_id), headers=headers)
    return r.status_code, r.content

def update_event(token, event_id, enterprise_name, client_name , information ,email, phone):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["EVENT"] + str(event_id), headers=headers).json()
    params = {}
    if pseudo == "blank":
        params["enterprise_name"] = r["enterprise_name"]
    else:
        params["enterprise_name"] = enterprise_name
    if first_name == "blank":
        params["client_name"] = r["client_name"]
    else:
        params["client_name"] = client_name
    if last_name == "blank":
        params["information"] = r["information"]
    else:
        params["information"] = information
    if email == "blank":
        params["email"] = r["email"]
    else:
        params["email"] = email
    if role == "blank":
        params["phone"] = r["phone"]
    else:
        params["phone"] = phone
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["EVENT"] + str(event_id) + "/", json=params, headers=headers)
    return r.status_code, r.content

def signup_all_event(token):
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["EVENT"], headers=headers)
    return r.status_code, r.content

def signup_one_event(token, event_id):
    headers = {'accept': 'application/json','Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["EVENT"] + str(event_id), headers=headers)
    return r.status_code, r.content