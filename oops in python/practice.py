#this is how we created class
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f"{self.__brand}"

    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


#this is how we created objects
#we have to define variable first and inside that we have to call class

tesla_car = ElectricCar("tesla", "model s", "85kWh")
print(tesla_car.fuel_type())

safari = Car("tata", "safari")
print(safari.fuel_type())
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())

# my_new_car = Car("tata", "safari")
# print(my_new_car.brand)
# print(my_new_car.model)