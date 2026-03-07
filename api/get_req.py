import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# status code print karo
print("Status Code:", response.status_code)

# JSON data nikalo
data = response.json()

# title print karo
print("Title:", data["title"])
