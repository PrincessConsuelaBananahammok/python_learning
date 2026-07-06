# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього
# декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. Властивості по
# типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька
# різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.


from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

    def get_area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"Rectangle: perimeter: {self.get_perimeter()}, area: {self.get_area()}"


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_perimeter(self):
        return self.__a + self.__b + self.__c

    def get_area(self):
        p = self.get_perimeter() / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

    def __str__(self):
        return f"Triangle: perimeter: {self.get_perimeter()}, area: {self.get_area()}"


class Parallelogram(Figure):
    def __init__(self, a, b, height):
        self.__a = a
        self.__b = b
        self.__height = height

    def get_perimeter(self):
        return 2 * (self.__a + self.__b)

    def get_area(self):
        return self.__a * self.__height

    def __str__(self):
        return f"Parallelogram: perimeter: {self.get_perimeter()}, area: {self.get_area()}"


figures = [Rectangle(1, 2),
           Triangle(3, 4, 5),
           Parallelogram(5, 6, 7)]

for figure in figures:
    print(figure)