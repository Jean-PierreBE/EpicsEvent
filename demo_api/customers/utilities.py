import requests
from demo_api.constants import END_POINT


def create_customer(token, enterprise_name, client_name, information, email, phone):
    params = {
        "enterprise_name": enterprise_name,
        "client_name": client_name,
        "information": information,
        "email": email,
        "phone": phone
    }
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.post(END_POINT["URL"] + END_POINT["CUSTOMER"], json=params, headers=headers)
    return r.status_code, r.content


def delete_customer(token, customer_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.delete(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id), headers=headers)
    return r.status_code, r.content


def update_customer(token, customer_id, enterprise_name, client_name, information, email, phone):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id), headers=headers).json()
    params = {}
    if enterprise_name == "blank":
        params["enterprise_name"] = r["enterprise_name"]
    else:
        params["enterprise_name"] = enterprise_name
    if client_name == "blank":
        params["client_name"] = r["client_name"]
    else:
        params["client_name"] = client_name
    if information == "blank":
        params["information"] = r["information"]
    else:
        params["information"] = information
    if email == "blank":
        params["email"] = r["email"]
    else:
        params["email"] = email
    if phone == "blank":
        params["phone"] = r["phone"]
    else:
        params["phone"] = phone
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + "/", json=params, headers=headers)
    return r.status_code, r.content


def signup_all_customer(token):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"], headers=headers)
    return r.status_code, r.content


def signup_one_customer(token, customer_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id), headers=headers)
    return r.status_code, r.content
