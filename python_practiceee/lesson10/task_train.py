class Train:
    def __init__(self):
        self.locomotive = Wagon(is_locomotive=True, number=1)
        self.wagons = []

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        return f"Train with {len(self.wagons)}: wagons {', '.join([str(k) for k in self.wagons])}"

    def add_wagon(self, number):
        # current_wagon= len(self.wagons) + 1
        if number not in [k.number for k in self.wagons]:
            self.wagons.append(wagon)
        pass

class Wagon:
    def __init__(self, is_locomotive=False, number=1):
        self.is_locomotive = is_locomotive
        # self.is_exception_passengers = True
        self.number = number
        self.passengers = []

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"Wagon #  {self.number}: {self.is_locomotive}"

    def add_passengers(self, passenger: dict):
        if len(self.passengers) is not 10:
            self.passengers.append(passenger)
        pass

train = Train()
print(train)
wg1 = Wagon(number=2)
wg1.add_passengers({"name": "Alex", "pass_number": "#7789"})
train.add_wagon(wg1)
print(train)
wagon = Wagon(number=2)


# class Locomotive(Wagon):
#     def __init__(self):
#         super().is_exception_passengers = False
#