from python_practiceee.lesson6.if_example import response



for number in range(1, 11):
    print(number)

names = ["John", "Michael", "David", "Den"]
ages = [22, 54, 44]
for name in names:
    print(name)

# for name in names:
#     print(name)
#     for age in ages:
#         print(age)

for _ in range(1, 11):
    print("hello")

# 8:36
response = [
    {"id": 1, "name": "Read only", "description": "For all users"},
{"id": 2, "name": "RW", "description": "For write and read"},
{"id": 3, "name": "all", "description": "admin"},
{"id": 3, "name": "all", "description": "admin"},
{"id": None, "name": "broken", "description": None}
]

for permission in response:
    if permission.get("id") is None:
        print("Permission denied")

# 8:40
uniq_ids = []
for perm in response:
    if perm.get("id") in uniq_ids:
        print("Ids are not uniq")
        break
    else:
        uniq_ids.append(perm.get("id"))

# break
# continue
# if element in list: True

for name in names:
    if name in "Den":
        continue
    print(f"You are not Den, {name}")

for k in range(10):
    if k == 20:
        break
else:
    print("Done")


