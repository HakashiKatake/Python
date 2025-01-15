
class Car:
    def __init__(self, make="Toyota", model="Corolla", year=2019):
        self.make = make
        self.model = model
        self.year = year

car = Car()
print(car.make, car.model, car.year)