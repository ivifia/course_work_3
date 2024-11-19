import requests
import json
def request():
    responce = requests.get('https://api.npoint.io/b7eaf584e7115dd76810').json()
    return responce