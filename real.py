import requests

url = "http://httpbin.org/headers"
response = requests.get(url)

if response.status_code == 200:
    print(response.content)
           