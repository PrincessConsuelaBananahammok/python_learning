string_example = "hello world"
tuple_example = (1, 2, 3)
list_string = list(string_example)
tuple_to_list = list(tuple_example)
print(list_string)
print(tuple_to_list)

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# що / звідки береться / при якій умові
list_comprehended = [num ** 2 for num in my_numbers if num % 2 == 1]
print(list_comprehended)
 # 20:47

sq_list = []
for num in my_numbers:
    if num % 2 == 1:
        sq_list.append(num**2)
print(sq_list)
print(list_comprehended)

my_range_num = range(10, 20)
print(list(my_range_num))

sq_list_100 = [k**2 for k in range(1, 100)]
print(sq_list_100)