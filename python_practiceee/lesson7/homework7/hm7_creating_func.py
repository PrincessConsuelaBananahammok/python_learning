print("Task1", "_" * 30)


def multiplication_table(number):
    multiplier = 1

    while multiplier * number <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


multiplication_table(3)

print("Task2", "_" * 30)


def sum_of_nums(num1, num2):
    result = num1 + num2
    return result


print(sum_of_nums(1, 2))

print("Task3", "_" * 30)


def avg_of_list(list1):
    return sum(list1) / len(list1)


print(avg_of_list([1, 2, 3, 4, 5]))

print("Task4", "_" * 30)


def reverse_line(line):
    return line[::-1]


print(reverse_line("hello word"))

print("Task5", "_" * 30)


def longest_word(list1):
    longest_w = max(list1, key=len)
    return longest_w


print(longest_word(["a", "bdddddd", "wewc"]))

print("Task6", "_" * 30)


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

print("Task7", "_" * 30, "check_uniq_symbols")


# some_text = input("Enter some text: ")
# uniq_symbols = set(some_text)
#
# count = len(uniq_symbols)
# if count > 10:
#     print(True)
# else:
#     print(False)

def check_uniq_symbols(some_text):
    uniq_symbols = set(some_text)
    return True if len(uniq_symbols) > 10 else False


print(check_uniq_symbols("lhbhvkfkdreswswa475d!"))

print("Task8", "_" * 30, "wait_for_the_letter")


# text = True
# while text:
#     text_with_h = input("Please enter some text with 'h' letter: ")
#     for letter in text_with_h:
#         if letter == 'h' or letter == 'H':
#             text = False

def wait_for_the_letter(letter):
    text = True
    while text:
        text_with_letter = input(f"Please enter some text with '{letter}' letter: ")
        if letter.lower() in text_with_letter or letter.upper() in text_with_letter:
            text = False


print(wait_for_the_letter("h"))

print("Task9", "_" * 30, "take_what_you_need")


# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst2 = []
# for el in lst1:
#     if type(el) == str:
#         lst2.append(el)
# print(lst2)

def take_what_you_need(lst, typ):
    result = [el for el in lst if isinstance(el, typ)]
    return result


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(take_what_you_need(lst1, str))

print("Task10", "_" * 30, "sum of even numbers")

# list_of_numbers = [10, 20, 23, 7, 55, 4]
# sum_of_numbers = 0
# for num in list_of_numbers:
#     if num % 2 == 0:
#         sum_of_numbers += num
# print(sum_of_numbers)

def sum_even_numbers(lst):
    sum_num = sum([num for num in lst if num % 2 == 0])
    return sum_num

print(sum_even_numbers([1, 2, 3, 4, 5]))