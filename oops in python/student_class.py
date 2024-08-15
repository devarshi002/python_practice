# Example 2: Student Class
# A class representing a student with attributes for name, grade, and major, and methods to get the student's info and determine if they are passing.

class Student:
    def __init__(self, name, grade, major):
        self.name =  name
        self.grade = grade
        self.major = major

    def get_info(self):
        return f"{self.name}, majoring in {self.major}, has a grade of {self.grade}"
    
    def is_passing(self):
        if self.grade >= 60:
            return f"{self.name} is pass the exam"



#usage
student1 = Student("Deva", 87, "Computer Engineering")
print(student1.get_info())
print(student1.is_passing())