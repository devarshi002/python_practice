class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age =age
    
    def get_info(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old"
    


#usage
dog1= Dog("Buddy", "Golden Retriever", 5)
print(dog1.get_info())