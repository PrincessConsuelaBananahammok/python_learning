# iter
# next()

list_of_numbers = [11, 12, 13, 14, 15]
list_of_numbers2 = [21, 22, 23, 24, 25]

# for el in list_of_numbers:
#     print(el)

iter_object = iter(list_of_numbers)
iter_object2 = iter(list_of_numbers2)

# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object2))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object2))
# print(next(iter_object))
# print(next(iter_object2))

try:
    while True:
        print(next(iter_object))
except StopIteration:
    pass

# for el in list_of_numbers:
#     print(el)

