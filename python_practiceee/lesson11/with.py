# менеджер контексту (тут файл автоматично закривається):
with open("example") as f:
    print(f.read())


try:
    # виконання магічного методу __enter__
    f = open("example")
    print(f.read())
finally:
    # виконання методу __exit__
    f.close()
