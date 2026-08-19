import requests


body = {
  "email": "test22naruto@test.com",
  "password": "Qwerty12345",
  "remember": False
}

url_signin = "https://qauto.forstudy.space/api/auth/signin"
url_get_current = "https://qauto.forstudy.space/api/users/current"

#створити сесію і заходити так - вар1
session = requests.Session()
session.post(url=url_signin, json=body)
# session.cookies.clear() - буде 401
response = session.get(url=url_get_current)

# заходити черезі кукі - вар2
# response_signin = requests.post(url=url_signin, json=body)
# cookie = dict(response_signin.cookies)
# response = requests.get(url=url_get_current, cookies=cookie)


print(response.status_code)
print(response.json())