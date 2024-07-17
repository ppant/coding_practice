import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

