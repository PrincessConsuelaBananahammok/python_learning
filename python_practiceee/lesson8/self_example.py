class Auto:
    def __init__(self, model, color, engine, fuel_to_km=0.2):
        self.model = model
        self.color = color
        self.engine = engine
        self.tank = 0
        self.__fuel_to_km = fuel_to_km

    def drive_to_nearest_town(self, distance_km):
        if self.tank / self.__fuel_to_km >= distance_km:
            self.tank = self.tank - distance_km * self.__fuel_to_km
            print("Driving")
        else:
            print(f"Can`t driving, have fuel only on {self.tank / self.__fuel_to_km} km")


class Nissan(Auto):
    brand = "NISSAN"

    @classmethod
    def say_greeting(cls):
        print(f"Hello, {cls.brand}!")


y61 = Nissan("y61", color="green", engine="3.0", fuel_to_km=0.1)
navara = Nissan("navara", color="red", engine="5.0")

print(navara.engine)
print(y61.model)

y61.tank = 50
y61.drive_to_nearest_town(400)
y61.drive_to_nearest_town(400)

navara.tank = 10
navara.drive_to_nearest_town(300)

Nissan.brand = "New Nissan"
navara.__class__.brand = "New Nissan"

print(navara.brand)
print(y61.brand)

