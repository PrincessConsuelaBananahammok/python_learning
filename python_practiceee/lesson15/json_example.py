import json
# Дані для запису у JSON-файл
user_data = [
    {"name": "John", "age": 30, "city": "New York", "is_active": True},
    {"name": "Alex", "age": 22, "city": "New York", "is_active": False},
    {"name": "Den", 'age': 33, "city": "New York", "has_friends": None}
]

user_data_json =json.dumps(user_data)
print(type(user_data_json))
print(user_data_json)

# with open("json_as_str.txt","w") as f:
#     f.write(user_data_json)

# with open("user_data.json","w") as f:
#     json.dump(user_data,f, indent=4)

# # Запис JSON-даних у файл
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

with open("json_as_str.txt") as f:
    data = json.loads(f.read())
print(type(data))
print(data)

with open("user_data.json") as f:
    data2 = json.load(f)
print(type(data2))
print(data2)
