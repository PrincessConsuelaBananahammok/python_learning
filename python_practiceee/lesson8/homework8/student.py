class Student:
    def __init__(self, name, surname, age, avg_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_score = avg_score

    def set_avg_score(self, avg_score):
        self.avg_score = avg_score

    def show_info(self):
        print(F"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Avg Score: {self.avg_score}")


student1 = Student("Naruto", "Uzumaki", 15, 44)

student1.show_info()

student1.set_avg_score(88)

student1.show_info()
