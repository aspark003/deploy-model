import requests
import gunicorn

url = "http://127.0.0.1:5000/model_prediction"
payload = {"features": [1.293665, 17.877919]}  # use real feature values

response = requests.post(url, json=payload)
print(response.json())

