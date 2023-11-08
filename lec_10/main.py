from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

class Plane(Vehicle):
    def __init__(self, make, model, year, wings):
        super().__init__(make, model, year)
        self.wings = wings

class Boat(Vehicle):
    def __init__(self, make, model, year, hull):
        super().__init__(make, model, year)
        self.hull = hull

class RaceCar(Car):
    def __init__(self, make, model, year, doors, top_speed):
        super().__init__(make, model, year, doors)
        self.top_speed = top_speed

car = Car("Toyota", "Camry", 2023, 4)
plane = Plane("Boeing", "747", 2000, 4)
boat = Boat("Sea-Doo", "Spark", 2022, 1)
race_car = RaceCar("Ferrari", "488 GTB", 2023, 2, 200)

print(car)
print(plane)
print(boat)
print(race_car)