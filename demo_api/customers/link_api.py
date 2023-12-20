import requests
from demo_api.constants import END_POINT, NULL_VALUE


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
    params["enterprise_name"] = r["enterprise_name"] if enterprise_name == NULL_VALUE else enterprise_name
    params["client_name"] = r["client_name"] if client_name == NULL_VALUE else client_name
    params["information"] = r["information"] if information == NULL_VALUE else information
    params["email"] = r["email"] if email == NULL_VALUE else email
    params["phone"] = r["phone"] if phone == NULL_VALUE else phone
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + "/", json=params, headers=headers)
    return r.status_code, r.content


def list_all_customer(token):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"], headers=headers)
    return r.status_code, r.content


def list_one_customer(token, customer_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id), headers=headers)
    return r.status_code, r.content
