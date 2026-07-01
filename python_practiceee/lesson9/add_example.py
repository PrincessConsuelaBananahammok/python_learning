# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other_point):
#         return Point(self.x + other_point.x, self.y + other_point.y)
#
# # Використання оператора додавання та автоматичний виклик __add__
# point1 = Point(1, 2)
# point2 = Point(3, 4)
# result = point1 + point2
# print(result.x, result.y)  # Виведе: 4 6

# 20:49

class Classes:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __add__(self, other):
        for k, v in other.__dict__.items():
            setattr(self, k, v)

    def __sub__(self):
        result = f"current classes\n"

        for k, v in self.__dict__.items():
            result += f"{k} has students: {v['students']} starts at {v['start']}\n"



class_one = ({"math": {"students": 100, "start": "22.10.2020"}})
print(class_one)
class_second = ({"phisics": {"students": 80, "start": "22.10.2020"}})

class_one += class_second