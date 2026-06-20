def is_even(number):
    return number % 2 == 0

print([num for num in range(20) if is_even(num)])
print(list(filter(is_even, range(20))))


# task
my_description = "My   name   is   Alex". split(" ")
print(my_description)

# var1
result = []
for k in my_description:
    if len(k):
        result.append(k)

print(result)

# var2
print(list(filter(len, my_description)))
print(filter(len, my_description))

filtered_list = list(filter(len, my_description))
print(filtered_list)
print(filtered_list[0])
print(my_description)

# var 3
print((k for k in my_description if len(k)))

# 20:01
