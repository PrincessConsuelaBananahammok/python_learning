print(all([True, True, True]))
print(all([True, True, False]))


def is_even(number):
    return number % 2 == 0


print(is_even(5))
print(is_even(6))
print(is_even(7))

result = [is_even(num) for num in [2, 4, 6, 10, 7]]
print(result)
print(all(result))
print("-"*80)
print(all([1,2,3]))
# all(bool(1),bool(2),bool(3)

print(any([0, False, ""]))
print(any([0, False, "Hello"]))
# -> bool(0) -> False, bool("Hello") -> True

print("-"*80)
print(bool(0))
print(int("1"))
print(list((1,2,3)))
