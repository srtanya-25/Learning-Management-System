import requests

url = "http://127.0.0.1:8000/api/v1/students/"

response = requests.get(url)

print("Status:", response.status_code)

if response.status_code == 200: 
    for i in response.json():
        print(f"{i['name']}")
else:
    print("Error")

