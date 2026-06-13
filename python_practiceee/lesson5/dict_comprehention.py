import random

dict_cmp = {number: number**2 for number in range(10)}
print(dict_cmp)

names = ["Alex", "Bob", "Ivan", "Sofa"]

dict_with_names = {number: random.choice(names) for number in range(10)}
print(dict_with_names)