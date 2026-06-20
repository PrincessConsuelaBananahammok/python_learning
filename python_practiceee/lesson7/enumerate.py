for k in enumerate(["den", "alex",]):
    print(k)

# print(type(enumerate(["den", "alex",])))

for k in enumerate(["den", "alex",], start=15):
    print(k)

for index, name in enumerate(["den", "alex",], start=15):
    print(f"Name:{index}, index:{name}")
