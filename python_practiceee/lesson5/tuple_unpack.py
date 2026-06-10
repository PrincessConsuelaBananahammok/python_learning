my_name, den_name, vik_name = ("Alex", "Rudy", "Bob")
print(den_name)

my_name = ("Alex", "Rudy")
print(*my_name)

my_name, *not_my_name, vikk_name = ("Alex", "Rudy", "Bob", "Ivan")
print(my_name)
print(not_my_name)
print(vikk_name)

some_text = 'placeholder'
tuple_text = tuple(some_text)
print(tuple_text)
print(list(my_name))

tuple_with_one_el = (23, )
not_tuple = (33)
print(type(tuple_with_one_el))
print(type(not_tuple))