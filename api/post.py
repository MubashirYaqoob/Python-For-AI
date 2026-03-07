import requests

url = "https://jsonplaceholder.typicode.com/posts"

# sending data 
payload = {
    "title" : "Mypost",
    "body" : "this is Ai "
}

response = requests.post(url,json=payload)

print("status code ",response.status_code)

print("response data",response.json())