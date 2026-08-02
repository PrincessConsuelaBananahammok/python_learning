import requests

url = "https://www.google.com/tia/tia.png"
response = requests.get(url)

with open("some_image.png", "wb") as f:
    f.write(response.content)

with open("some_image.png", "rb") as f:
    files = { "image": f}

    upload_response = requests.post("http://127.0.0.1:8080/upload",files=files)



filename = "some_image.png"
response = requests.get(f"http://127.0.0.1:8080/image/{filename}",headers={"Content-Type": "text"})


response = requests.delete(f"http://127.0.0.1:8080/delete/{filename}")
print(response.json())


response = requests.get(f"http://127.0.0.1:8080/image/{filename}",headers={"Content-Type": "text"})
print(response.json())


