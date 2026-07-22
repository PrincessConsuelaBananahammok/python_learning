file_path = "file_for_read_write.txt"

# r - reading
# w - write, режим запису або перестворення файлу
# a - append, додавання в файл, або створиться якщо файл відсутній

# r+ - читання + write , file should exist
# w+ - читання + запис, але файл може бути відсутній
# a+ - read + append , file can be absent


with open(file_path, mode="w") as f:
    f.write("line1\n")
    f.write("line2")
    f.write("line3\n\t")
    f.write(r"line4\n")
    f.write(" line4\\\n")

    f.write("""\n\n first row
    second row
last row
""")
    f.writelines(["line5\n", "line6\n", "line7\n", "line8\n"])


# with open(file_path, mode="a") as f:
#     f.write("line1\n")
#     f.write("line2")

with open(file_path, mode="r") as f:
    data = f.read()
    print(data)

with open(file_path, mode="r") as f:
    data = f.readlines()
    print(data)

with open(file_path, mode="r") as f:
    print(f.readlines())
    print(f.readlines())
    print(f.readlines())
    print(f.readlines())