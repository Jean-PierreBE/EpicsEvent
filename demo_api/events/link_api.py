import requests
from demo_api.constants import END_POINT, NULL_VALUE
from urllib.parse import urlencode


def create_event(token, customer_id, contract_id, begin_date, begin_hour, end_date, end_hour, location,
                 notes, attendees_count, support_user):
    params = {
        "begin_date": begin_date,
        "begin_hour": begin_hour,
        "end_date": end_date,
        "end_hour": end_hour,
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


def update_event(token, customer_id, contract_id, event_id, begin_date, begin_hour, end_date, end_hour, location, notes,
                 attendees_count, support_user):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"] + str(event_id), headers=headers).json()
    params = {}
    params["begin_date"] = r["begin_date"] if begin_date == NULL_VALUE else begin_date
    params["begin_hour"] = r["begin_hour"] if begin_hour == NULL_VALUE else begin_hour
    params["end_date"] = r["end_date"] if end_date == NULL_VALUE else end_date
    params["end_hour"] = r["end_hour"] if end_hour == NULL_VALUE else end_hour
    params["location"] = r["location"] if location == NULL_VALUE else location
    params["notes"] = r["notes"] if notes == NULL_VALUE else notes
    params["attendees_count"] = r["attendees_count"] if attendees_count == NULL_VALUE else attendees_count
    params["support_user"] = r["support_user"] if support_user == NULL_VALUE else support_user
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.put(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"] + str(event_id) + "/", json=params, headers=headers)
    return r.status_code, r.content


def list_all_event(token, customer_id, contract_id, params={}):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    query_params = ''
    if params:
        query_params = '?' + urlencode(params)
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"] + query_params, headers=headers)
    return r.status_code, r.content


def list_one_event(token, customer_id, contract_id, event_id):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + token}
    r = requests.get(END_POINT["URL"] + END_POINT["CUSTOMER"] + str(customer_id) + END_POINT["CONTRACT"] +
                     str(contract_id) + END_POINT["EVENT"] + str(event_id), headers=headers)
    return r.status_code, r.content
