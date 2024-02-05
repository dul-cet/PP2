"""
3. Define a class named `Rectangle` which inherits from `Shape` class from task 2. 
Class instance can be constructed by a `length` and `width`.
The `Rectangle` class has a method which can compute the `area`.
"""

class Shape:
    def __init__(self):
        self.area = 0

    def area(self):
        print(f"The area of the shape is: {self.area}")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def compute_area(self):
        self.area = self.length * self.width
        print(f"The area of the rectangle is: {self.area}")

rectangle = Rectangle(5, 6)
rectangle.compute_area()