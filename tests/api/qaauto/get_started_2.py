import requests
from settings import settings


body = {
  "email": settings.USER_EMAIL,
  "password": settings.USER_PASS,
  "remember": False
}

url_signin = f"{settings.QA_AUTO_API_URL}/auth/signin"
url_get_current = f"{settings.QA_AUTO_API_URL}/users/current"

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