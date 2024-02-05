"""
2. Define a class named `Shape` and its subclass `Square`. 
The `Square` class has an `init` function which takes a `length` as argument.
Both classes have a `area` function which can print the area of the shape where Shape's area is 0 by default.
"""

class Shape:
    def __init__(self):
        self._area = 0 

    def calculate_area(self):
        print(f"The area of the shape is: {self._area}")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self._area = length ** 2

square = Square(5)
square.calculate_area()