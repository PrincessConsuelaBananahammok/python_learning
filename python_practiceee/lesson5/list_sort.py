my_list_names = ["Alex", "Rudy", "Bob"]
my_list_ages = [2, 5, 33, 3, 66]

sorted_names = sorted(my_list_names)
print(sorted_names)
sorted_ages = sorted(my_list_ages, reverse=True)
print(sorted_ages)

# # змінює першочерговий список
# print(my_list_ages)
# my_list_ages.sort()
# print(my_list_ages)

# _________________________________________
# var 1
def my_fn(word):
    word_lenth = len(word)
    return word_lenth

# var 2 lambda arg: action with arg
sorted_names_custom_lambda = sorted(my_list_names, key=lambda x: len(x))
sorted_names_custom = sorted(my_list_names, key=my_fn)

print(sorted_names_custom)
print(sorted_names_custom_lambda)
# ___________________________________________




