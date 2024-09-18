import requests
import pprint

params = {
    "userId": 1
}

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url, params=params)
print(response.status_code, response.ok)

print(response.text)


