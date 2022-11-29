import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_res = requests.post(endpoint, params={"abc": 123}, json={
    "title": "hello world"})
# HTTP REQ

print(get_res.json())
print(get_res.status_code)
