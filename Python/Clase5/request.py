import requests

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)

print(response.status_code)
jsonResponse = response.json()
print(jsonResponse)