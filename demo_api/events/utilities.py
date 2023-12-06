import requests
from demo_api.constants import END_POINT


def create_event(token, customer_id, contract_id, client_name, email, phone, begin_date, end_date, location, notes,
                 attendees_count, support_user):
    params = {
        "client_name": client_name,
        "email": email,
        "phone": phone,
        "begin_date": begin_date,
        "end_date": end_date,
        "location": location,
        "notes": notes,
        "attendees_count": attendees_count,
        "support_user": support_user
    }
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.post(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                      str(contract_id) + END_POINT["EVENT"], json=params, headers=headers)
    return r.status_code, r.content


def delete_event(token, customer_id, contract_id, event_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.delete(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                        str(contract_id) + END_POINT["EVENT"] + str(event_id), headers=headers)
    return r.status_code, r.content


def update_event(token, customer_id, contract_id, event_id, client_name, email, phone, begin_date, end_date,
                 location, notes, attendees_count, support_user):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"] + str(event_id), headers=headers).json()
    params = {}
    if client_name == "blank":
        params["client_name"] = r["client_name"]
    else:
        params["client_name"] = client_name
    if email == "blank":
        params["email"] = r["email"]
    else:
        params["email"] = email
    if phone == "blank":
        params["phone"] = r["phone"]
    else:
        params["phone"] = phone
    if begin_date == "blank":
        params["begin_date"] = r["begin_date"]
    else:
        params["begin_date"] = begin_date
    if end_date == "blank":
        params["end_date"] = r["end_date"]
    else:
        params["end_date"] = end_date
    if location == "blank":
        params["location"] = r["location"]
    else:
        params["location"] = location
    if notes == "blank":
        params["notes"] = r["notes"]
    else:
        params["notes"] = notes
    if attendees_count == "blank":
        params["attendees_count"] = r["attendees_count"]
    else:
        params["attendees_count"] = attendees_count
    if support_user == "blank":
        params["support_user"] = r["support_user"]
    else:
        params["support_user"] = support_user
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"] + str(event_id) + "/", json=params, headers=headers)
    return r.status_code, r.content


def signup_all_event(token, customer_id, contract_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"], headers=headers)
    return r.status_code, r.content


def signup_one_event(token, customer_id, contract_id, event_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"] + str(event_id), headers=headers)
    return r.status_code, r.content
