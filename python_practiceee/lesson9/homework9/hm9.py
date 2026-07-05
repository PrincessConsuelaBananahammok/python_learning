# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Rhombus:
    def __init__(self, len_a, angle_a):
        self.len_a = len_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "len_a":
            if value <= 0:
                print("len_a must be > 0")
            else:
                super().__setattr__(key, value)
        elif key == "angle_a":
            if value <= 0:
                print("angle_a must be > 0")
            else:
                super().__setattr__(key, value)
                super().__setattr__("angle_b", (180 - value))
        elif key == "angle_b":
            print("angle_b is calculated automatically")
        else:
            super().__setattr__(key, value)


        # elif key == "angle_b":
        #     if value + self.angle_a != 180:
        #         print("angle_a + angle_b must be 180 degrees")
        #     else:
        #         super().__setattr__(key, value)

r = Rhombus(-5, 60)
# r.len_a = -5

print(r.len_a)
# print(r.angle_a)
# print(r.angle_b)
# r.angle_a = 100
# print(r.angle_a)
# print(r.angle_b)
#
# r = Rhombus(0, 60)
#
#
#
# r2 = Rhombus(5, 60)
# print(r2.len_a, r2.angle_a, r2.angle_b)
#
# r2.angle_a = 100
# print(r2.angle_a, r2.angle_b)
#
# r2.len_a = 10
# print(r2.len_a)
#
# r2.angle_b = 50
# print(r2.angle_a, r2.angle_b)




