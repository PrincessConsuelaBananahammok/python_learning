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

    def go_somewhere(self, amount_in_km):
        if self.tank >= amount_in_km:
            self.tank -= amount_in_km
            print("Driving")
        else:
            print("Can`t drive, have not enough fuel")

x5 = Car(brand="BMW", model="X5")
x5.set_tank(60)
x5.go_somewhere(40)
x5.go_somewhere(50)

polo = Car(brand="VW", model="Polo")
polo.go_somewhere(40)