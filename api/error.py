import requests

url = "https://jsonplaceholder.typicode.com/invalid"

response= requests.get(url)

if response.status_code != 200:
    print("request failed")
else :
    print("request worked")