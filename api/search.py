import requests

url = "https://jsonplaceholder.typicode.com/comments"

response =  requests.get(url)
data = response.json()

for i in data :
    if i["postId"] == 1:
        print("Name",i["name"])
        print("Email",i["email"])
else:
 print("Request is failed")
        
