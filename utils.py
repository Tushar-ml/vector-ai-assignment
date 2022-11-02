import requests
import json


def stream_model_api(message):
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }

    message = json.dumps({"data": message})
    response = requests.post('http://localhost:8000/predict',
                             headers=headers, data=message)
    print(response)
