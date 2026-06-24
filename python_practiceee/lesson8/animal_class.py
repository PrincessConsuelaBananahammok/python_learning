class Animal:
    def make_sound(self):
        print("Animal sound")

    # def dog_sound(self):
    #     print("Grrr!")
    #
    # def cat_sound(self):
    #     print("Meow")

    def go_sleep(self):
        print("Sleeping...")


class Dog(Animal):
    def make_sound(self):
        print("Grrr!")


class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bug(Animal):
    pass


dog = Animal()
cat = Animal()
dog.make_sound()
cat.make_sound()

# dog.dog_sound()

dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()

unknown_animal = Animal()
unknown_animal.make_sound()

bug = Bug()
bug.make_sound()

dog.go_sleep()
cat.go_sleep()
bug.go_sleep()
