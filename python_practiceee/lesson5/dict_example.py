# ключі унікальні і хешабельні


my_dict = {"name": "Alex", "age": 35, "has_job": True}
print(my_dict)

my_dict["new_key"] = "new_value"
my_dict["new_key"] = "old_value"
print(my_dict)

new_dict_update = {"key": "new_value"}
my_dict.update(new_dict_update)
print(my_dict)

# get

print(my_dict["name"])

print(my_dict.get("key1"))
print(my_dict.get("key0", "Alex default"))

print(my_dict.get("new_key", "Alex default").get("key1"))

