# Example 3: Rectangle Class
# A class representing a rectangle with attributes for width and height and methods to calculate the area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area_of_rect = self.width * self.height
        return(area_of_rect)
    
    def perimeter(self):
        perimeter_of_rect = 2* (self.width + self.height)
        return(perimeter_of_rect)

#usage
Rectangle1 = Rectangle(5, 10)
print(Rectangle1.area())
print(Rectangle1.perimeter())