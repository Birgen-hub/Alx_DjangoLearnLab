import requests

url = "http://127.0.0.1:8000/api/accounts/login/"
data = {
    "username": "hi",
    "password": "Birgen@99"
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:", response.json())
