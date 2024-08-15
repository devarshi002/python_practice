# Example 7: Employee Class
# A class representing an employee with attributes for name, position, and salary, and methods to give a raise and get employee info.

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    

    def give_rise(self, amount):
        self.salary += amount
        print(f"{self.name} got a raise of {amount}. New salay is {self.salary}.")


    def get_info(self):
        return f"{self.name} work as {self.position} with a salary of {self.salary}"
    


#usage
employee1 = Employee("Devarshi tambulkar", "python developer", 90000)
print(employee1.get_info())
employee1.give_rise(10000)