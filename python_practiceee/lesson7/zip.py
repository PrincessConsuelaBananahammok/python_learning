my_description = "My   name   is   Alex".split(" ")

len_of_desc = list(map(len, my_description))

print(my_description)
print(len_of_desc)

print(list(zip(my_description, len_of_desc)))
print(list(zip(my_description, len_of_desc, range(20))))