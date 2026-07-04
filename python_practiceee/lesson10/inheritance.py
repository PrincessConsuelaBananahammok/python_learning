from python_practiceee.lesson9.str_example import user


class Animal:
    def make_sound(self):
        print("Animal sound")

    # def dog_sound(self):
    #     print("Grrr!")
    #
    # def cat_sound(self):
    #     print("Meow")

    def walk(self):
        print("Walking...")

    def go_sleep(self):
        print("Sleeping...")


class Lion(Animal):
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def make_sound(self):
        print("Grrr!")


class Bird(Animal):
    def __init__(self, name):
        self.name = name
        self.wings = 2
        self.tail = "Flufy"

    def make_sound(self):
        print("Chiric")

class Bug(Animal):
    pass

# dog = Dog()
# print(dog.make_sound())

class Hymera(Lion, Bird):

    def __init__(self, name):
        # v1
        super().__init__(name)

        # self.name = name
        # v2
        # Lion.__init__(self, name)
        # Bird.__init__(self, name)


pushok = Hymera("Pushok")
print(pushok.name)
print(pushok.legs)
print(pushok.wings)
print(pushok.tail)
pushok.make_sound()
print(Hymera.mro())

# class User:
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return 'User'
#
#     def str(self):
#         return super.__str__("1")
#
#     def str_2(self):
#         return super().__str__()
#
# class Student(User):
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return 'Student'
#
#     def str(self):
#         return super.__str__("2")
#
#     def str_2(self):
#         return super().__str__()
#
# class Admin(User):
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return 'Admin'
#
#     def str(self):
#         return super.__str__("3")
#
#     def str_2(self):
#         return super().__str__()
#
# class SuperAdmin(Admin):
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return 'Super Admin'
#
#     def str(self):
#         return super.__str__("4")
#
#     def str_2(self):
#         return super().__str__()
#
# user = User()
# print(user)
#
# student = Student()
# print(student)
#
# admin = Admin()
# print(admin)
#
# super_admin = SuperAdmin()
# print(super_admin)
#
# print(user.str())
# print(user.str_2())
#
# print(student.str())
# print(student.str_2())
#
# print(admin.str())
# print(admin.str_2())
#
# print(super_admin.str())
# print(super_admin.str_2())
#
# test = super()
# print(test)