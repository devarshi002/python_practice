# 1. Person Class with Property Decorators
# This class uses property decorators to control access to attributes, ensuring encapsulation.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")
        
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            raise ValueError("Age must be a positive integer")
        
        
    def display_info(self):
        return f"Name : {self.name}, Age : {self.age}"
    
#usage
person1 = Person("Deva", 21)
print(person1.display_info())

person1.name = "Rahul"
person1.age = 22
print(person1.display_info())