def some_function(a, b):
    print(a + b)
    return a + b


def factorial(n):
    if n < 0:
        raise ValueError('n must be non-negative')

    if type(n) != int:
        raise TypeError('n must be an integer')

    if n == 0:
        return 1

    else:
        return n * factorial(n-1)