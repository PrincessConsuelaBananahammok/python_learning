# def greeting(name):
#     print(f"Hello {name}")
#
# def greeting2(name):
#     print(f"Hello {name}")
#
# def good_morning(fn, name):
#     print("Good Morning")
#     fn(name)

# good_morning(greeting, "Bob")
# good_morning(greeting2, "John")

# my_new_function = greeting
# my_new_function("Den")
# print(id(greeting))
# print(id(my_new_function))

def greeting_decorator(function):
    def wrapper(*args, **kwargs):
        print("Good morning!")
        return function(*args, **kwargs)
    return wrapper

@greeting_decorator
def greeting(name):
    print(f"Hello, {name}!")

@greeting_decorator
def something_else(list_, age):
    for el in list_:
        print(el + age)


greeting("Bob")