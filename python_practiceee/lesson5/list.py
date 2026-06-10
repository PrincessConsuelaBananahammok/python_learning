# mutable, iterable - list

my_list_names = ["Alex", "Rudy", "Bob"]
print(my_list_names)
print(id(my_list_names))

# append
my_list_names.append("Viktor")
print(my_list_names)
print(id(my_list_names))

# extend
additional_list = [1, 2, 3]
my_list_names.extend(additional_list)
print(my_list_names)

# insert
my_list_names.insert(1,"Sofa")
print(my_list_names)

# pop
last_element = my_list_names.pop()
print(last_element)
print(my_list_names)

second_from_end = my_list_names.pop(-2)
print(second_from_end)
print(my_list_names)

# remove
my_list_names.append("Rudy")
print(my_list_names)
print(id(my_list_names))
my_list_names.remove("Rudy")
print(my_list_names)

my_list_names.append("Rudy")
my_list_names.append("Rudy")

print(my_list_names)
element_to_delete = "Rudy"
list_of_rudy = []
for item in my_list_names:
    if item == element_to_delete:
        list_of_rudy.append(item)
for item in list_of_rudy:
    my_list_names.remove(item)

print(my_list_names)
print(list_of_rudy)

# 20:05

# variant 2
alex_count = my_list_names.count(element_to_delete)
while alex_count > 0:
    my_list_names.remove(element_to_delete)
    alex_count -= 1