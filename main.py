import requests
import pprint

data = {

    "title" : "foo",

    "body" : "bar",

    "userId" : 1

}

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(url, data=data)
print(response.status_code, response.ok)

print(f"ответ - {response.json()}")


