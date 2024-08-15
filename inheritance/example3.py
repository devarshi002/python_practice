# Example 3: Inheriting and Extending Methods

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"Employee : {self.name}, Salary : {self.salary}"
    

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        basic_details = super().get_details()
        return f"{basic_details}, Department : {self.department}"
    


#usage
employee = Employee("Deva", 50000)
manager = Manager("Rahul", 60000, "IT")
print(employee.get_details())
print(manager.get_details())