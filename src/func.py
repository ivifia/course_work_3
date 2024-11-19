from src.utils import request
from datetime import datetime


def executed():
    execute_date = []
    operation=request()
    for i in range(len(operation)):
        if operation[i].get("state")=="EXECUTED":
            execute_date.append(operation[i])
    execute_date.sort(key=lambda x: datetime.fromisoformat(x["date"]), reverse=True)
    return execute_date[:5]



def card (operation):
    return f"{operation[:-16]}{operation[-16:-12]} {operation[-12:-10]}** **** {operation[-4:]}"



def check(operation):
    return f"**{operation[-4:]}"