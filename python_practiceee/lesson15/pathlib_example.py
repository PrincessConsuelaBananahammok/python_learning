import pathlib
from functools import partial

from constants import BASE_PROJECT_PATH
import os

current_directory = pathlib.Path().absolute()
root_dir = pathlib.Path().absolute().parent

# print(type(current_directory))
# print(current_directory)
# print(current_directory.name)
# print(current_directory.parent)

parents = current_directory.parents

# for par in parents:
#     print(par.name)


# for path_ in current_directory.iterdir():
#     if path_.is_file():
#         print(path_.name)

# print("*" * 90)
#
# for path_ in current_directory.iterdir():
#     if path_.is_dir():
#         print(path_.name)

# for path_ in root_dir.iterdir():
#     if path_.is_file():
#         print(path_.name)
#
# print("*" * 90)
#
# for path_ in root_dir.iterdir():
#     if path_.is_dir():
#         print(path_.name)



# lesson4_full_path = os.path.join(str(current_directory), "lesson4")
#
#
# for path_ in pathlib.Path(lesson4_full_path).iterdir():
#     if path_.is_file():
#         print(path_.name)
#
# print("*" * 90)
#
# for path_ in pathlib.Path(lesson4_full_path).iterdir():
#     if path_.is_dir():
#         print(path_.name)

file_to_find = "homework_04.py"

for current_path, folders, files in os.walk(BASE_PROJECT_PATH):
    if file_to_find in files:
        print(os.path.join(current_path, file_to_find))

partial_file_name = "string"

for current_path, folders, files in os.walk(BASE_PROJECT_PATH):
    for file in files:
        if partial_file_name in file:
            print(os.path.join(current_path, partial_file_name))

