import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_res = requests.get(endpoint, params={"abc": 123}, json={
                       "query": "hello world"})
# HTTP REQ

print(get_res.json())
print(get_res.status_code)
