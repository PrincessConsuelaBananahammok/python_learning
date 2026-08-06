

def even_nums_generator(num):
    for x in range(0, num+1):
        if x % 2 == 0:
            yield x

gen = even_nums_generator(10)
for num in gen:
    print(num)

def fibonacci_generator(n):
    a = 0
    b = 1

    while a <= n:
        yield a
        a, b = b, a + b


for num in fibonacci_generator(7):
    print(num)




