from demo_api.constants import NULL_VALUE
def format_date_json(date_str, time_str):
    print(date_str)
    print(time_str)
    return date_str[6:10] + "-" + date_str[3:5] + "-" + date_str[0:2] + "T" + time_str

def reformat_date(date_old, date_new, time_new):
    if date_new == NULL_VALUE:
        if time_new == NULL_VALUE:
            return date_old
        else:
            return format_date_json(date_old[0:10],time_new)
    else:
        if time_new == NULL_VALUE:
            return format_date_json(date_new,date_old[11:16])
        else:
            return format_date_json(date_new,time_new)