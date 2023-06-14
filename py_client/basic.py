import requests

# endpoint = "https://httpbin.org/200/"
endpoint2 = "http://localhost:8000/api/"

get_response = requests.get(endpoint2, json={"content": "Some random content"})
print(get_response.json())

