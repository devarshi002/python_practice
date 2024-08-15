# Example 1: Simple Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    
    def speak(self):
        return "The animal make a sound."
    

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: woof!"


#usage
animal = Animal("Generic Animal")
dog = Dog("buddy")
print(animal.speak())
print(dog.speak())

    