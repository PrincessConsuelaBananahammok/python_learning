#set hash values uniq

my_set = {1, 2, 3, 3}
print(my_set)

# my_set = {1, [1, 2]} - error

my_set.add(4)
my_set.add(5)

some = my_set.pop()
print(my_set)

my_set.remove(5)


list_if_ids = [1111, 1002, 1002, 1234, 2342]
len_list = len(list_if_ids)
len_set = len(set(list_if_ids))
print(len_list)
print(len_set)

actual_list_of_users = ["Alex", "Bob", "Ivan", "Sofa"]
expected_list_of_users = ["Alex", "Bob", "Sofa", "Ivan"]

print(actual_list_of_users == expected_list_of_users)
print(set(actual_list_of_users) == set(expected_list_of_users))
