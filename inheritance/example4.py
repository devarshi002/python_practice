# Example 4: Using Multiple Levels of Inheritance

class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)

# Usage
rectangle = Rectangle("Blue", 5, 10)
square = Square("Red", 4)

print(rectangle.get_color())  # Output: Blue
print(rectangle.area())       # Output: 50
print(square.get_color())     # Output: Red
print(square.area())          # Output: 16