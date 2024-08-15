# Example 2: Adding New Attributes and Methods

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"The {self.brand} {self.model} starts"
    

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def honk(self):
        return "beep Beep!"
    

#usage
vehicle = Vehicle("bullet", "classic 350")
car = Car("tata", "nexon", 4)

print(vehicle.start())
print(car.start())
print(car.honk())