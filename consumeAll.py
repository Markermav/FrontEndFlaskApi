import requests


def responseGet():

    URL = "http://127.0.0.1:8000/all"

    r = requests.get(url=URL)
    data = r.json()
    return data