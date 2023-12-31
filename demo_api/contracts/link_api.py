import requests
from demo_api.constants import END_POINT, NULL_VALUE
from urllib.parse import urlencode


def create_contract(token, customer_id, sign_date, amount_contract, saldo_contract, status_contract):
    params = {
        "sign_date": sign_date,
        "amount_contract": amount_contract,
        "saldo_contract": saldo_contract,
        "status_contract": status_contract
    }
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.post(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"],
                      json=params, headers=headers)
    return r.status_code, r.content


def delete_contract(token, customer_id, contract_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.delete(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                        str(contract_id), headers=headers)
    return r.status_code, r.content


def update_contract(token, customer_id, contract_id, sign_date, amount_contract, saldo_contract, status_contract):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id), headers=headers).json()
    params = {}
    params["sign_date"] = r["sign_date"] if sign_date == NULL_VALUE else sign_date
    params["amount_contract"] = r["amount_contract"] if amount_contract == NULL_VALUE else amount_contract
    params["saldo_contract"] = r["saldo_contract"] if saldo_contract == NULL_VALUE else saldo_contract
    params["status_contract"] = r["status_contract"] if status_contract == NULL_VALUE else status_contract
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + "/", json=params, headers=headers)
    return r.status_code, r.content


def list_all_contract(token, customer_id, params={}):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    query_params = ''
    if params:
        query_params = '?' + urlencode(params)
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) +
                     END_POINT["CONTRACT"] + query_params, headers=headers)
    return r.status_code, r.content


def list_one_contract(token, customer_id, contract_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id), headers=headers)
    return r.status_code, r.content
