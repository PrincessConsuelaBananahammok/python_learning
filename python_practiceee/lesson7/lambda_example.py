def count_h(word):
    return word.count("h")


print(id("hello"))

new_fn = count_h

print(count_h("hello"))

print(new_fn("hhhello"))

print(max([1,2,3]))
print(max(["hh", "hello"], key=count_h))
print(max(["hh", "hello"], key=lambda x:x.count("h")))

new_lambda = lambda x: x * 2
print(new_lambda("hello"))


new_new_lambda = lambda x,y: pow(x,y)
print(new_new_lambda(2, 5))