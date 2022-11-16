import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_res = requests.get(endpoint)
print(get_res.text)
print(get_res.status_code)
