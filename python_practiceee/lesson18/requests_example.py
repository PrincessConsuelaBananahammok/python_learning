import requests
#pip install requests

response = requests.get(url= "https://swapi.info/api/people/1")

pass

status_code = response.status_code
text = response.text
headers = dict(response.headers)

response_json = response.json()
#json.loads(response.text)

print("status code", status_code)
print("headers", headers)
print("text", text)
print("-" * 90)
print("response_json", response_json)

print(response_json.get("name"))