
some_text = input("Enter some text: ")
uniq_symbols = set(some_text)

count = len(uniq_symbols)
if count > 10:
    print(True)
else:
    print(False)