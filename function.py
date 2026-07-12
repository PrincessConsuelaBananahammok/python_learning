def some_function(a, b):
    print(a + b)
    return a + b


def factorial(n):
    if n < 0:
        raise ValueError('n must be non-negative')

    if type