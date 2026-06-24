class Car:
    # atribute
    class_name = "Car class"
    # class method
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.tank = 0

    def set_tank(self, value):
        self.tank = value
# instance
x5 = Car(brand="BMW", model="X5")
print(x5.brand, x5.model)

polo = Car(brand="VW", model="Polo")
print(polo.brand, polo.model)

polo.tank = 50
print(polo.tank)

polo.set_tank(100)

print(x5.tank)

print(x5.class_name)
print(polo.class_name)