# Опишіть об'єкт поїзд. Клас повинен містити поля та метод для додавання вагонів
# (необхідно додати об`єкти та екземпляри класу вагонів)
#
# В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
# Опишіть клас Вагон  разом із поїздом. Вагон повинен містити список пасажирів і дозволяти додавати пасажирів.
# У вагоні може бути не більше 10
#
# Під час використання функції len у вагоні я хочу бачити кількість пасажирів
# Використовуючи len у поїзді, я хочу бачити список вагонів без локомотива. Кожен вагон повинен мати номер.



class Train:
    def __init__(self, name, locomotive: Locomotive):
        self.name = name
        self.list_train_units = [locomotive]

    def __len__(self):
        return len([item for item in self.list_train_units if isinstance(item, Carriage)])

    def add_carriage(self, carriage):
        carriage.number = len(self) + 1
        self.list_train_units.append(carriage)


class TrainUnit:
    def __init__(self, number):
        self.number = number


class Locomotive(TrainUnit):
    def __init__(self, number):
        super().__init__(number)


class Carriage(TrainUnit):
    def __init__(self):
        super().__init__(None)
        self._list_passengers = []

    def __len__(self):
        return len(self._list_passengers)

    def add_passenger(self, passenger):
        if len(self) < 10:
            self._list_passengers.append(passenger)
        else:
            print("You can't add more passengers")


class Passenger:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

locomotive = Locomotive(0)
train = Train("Intercity", locomotive)
print(len(train))

carriage1 = Carriage()
carriage2 = Carriage()
carriage3 = Carriage()

train.add_carriage(carriage1)
train.add_carriage(carriage2)
train.add_carriage(carriage3)

print(carriage1.number)
print(carriage2.number)
print(carriage3.number)

print(len(train))

p1 = Passenger("Іван", "Петренко", 25)
p2 = Passenger("Олена", "Іваненко", 31)
p3 = Passenger("Марія", "Коваль", 18)

carriage1.add_passenger(p1)
carriage2.add_passenger(p2)
carriage1.add_passenger(p3)

print(len(carriage2))

print(train.list_train_units)