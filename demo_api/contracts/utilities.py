import requests
from demo_api.constants import END_POINT


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
    if sign_date == "blank":
        params["sign_date"] = r["sign_date"]
    else:
        params["sign_date"] = sign_date
    if amount_contract == "blank":
        params["amount_contract"] = r["amount_contract"]
    else:
        params["amount_contract"] = amount_contract
    if saldo_contract == "blank":
        params["saldo_contract"] = r["saldo_contract"]
    else:
        params["saldo_contract"] = saldo_contract
    if status_contract == "blank":
        params["status_contract"] = r["status_contract"]
    else:
        params["status_contract"] = status_contract
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + "/", json=params, headers=headers)
    return r.status_code, r.content


def signup_all_contract(token, customer_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    print(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"])
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) +
                     END_POINT["CONTRACT"], headers=headers)
    return r.status_code, r.content


def signup_one_contract(token, customer_id, contract_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id), headers=headers)
    return r.status_code, r.content
