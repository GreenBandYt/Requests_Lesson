import requests
import pprint

params = {
    "q": "python"
}

url = "https://api.github.com/search/repositories"
response = requests.get(url, params=params)
print(response.status_code, response.ok)

pprint.pprint(response.json())


