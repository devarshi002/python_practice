# Example 5: Circle Class
# A class representing a circle with attributes for radius and methods to calculate the area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius **2)
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
#usage
circle1 = Circle(5)
print(f"Area : {circle1.area()}")
print(f"Circumference: {circle1.circumference()}")
        