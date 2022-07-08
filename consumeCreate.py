import requests
import json


def createBooks(name, price, image):

    URL = "http://127.0.0.1:8000/create"
    payload = {
         'name': name,
         'price': price,
         'image': image
    }
    headers = {
        'Content-type':'application/json', 
        'Accept':'application/json'
    }
    files = {}

    jsonPayload =  json.dumps(payload)
    print(jsonPayload)
    response = requests.request("POST", URL, headers=headers, data=jsonPayload, files=files)
   
    print(response)
    


