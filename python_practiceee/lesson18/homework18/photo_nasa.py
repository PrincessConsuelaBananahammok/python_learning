import requests
import json

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}


response = requests.get(search_url, params=search_params)
response_json = response.json()

nasa_id = response_json["collection"]["items"][0]["data"][0]["nasa_id"]


nasa_ids = []
for item in response_json["collection"]["items"]:
    nasa_ids.append(item["data"][0]["nasa_id"])


asset_url_template_1 = f"{BASE_URL}/asset/{nasa_ids[0]}"
response_1 = requests.get(asset_url_template_1)

image_url_1 = response_1.json()["collection"]["items"][0]["href"]
image_response_1 = requests.get(image_url_1)

with open("mars_photo1.jpg", "wb") as f:
    f.write(image_response_1.content)

asset_url_template_2 = f"{BASE_URL}/asset/{nasa_ids[1]}"
response_2 = requests.get(asset_url_template_2)

image_url_2 = response_2.json()["collection"]["items"][0]["href"]
image_response_2 = requests.get(image_url_2)

with open("mars_photo2.jpg", "wb") as f:
    f.write(image_response_2.content)


