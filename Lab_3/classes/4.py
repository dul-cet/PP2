"""
4. Write the definition of a Point class. Objects from this class should have a
    - a method `show` to display the coordinates of the point
    - a method `move` to change these coordinates
    - a method `dist` that computes the distance between 2 points
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"The coordinates of the point are: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"The point has been moved to: ({self.x}, {self.y})")

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

point1 = Point(2, 3)
point2 = Point(5, 7)
point1.show()
point2.show()
point1.move(3, -2)
point1.show()
point2.show()
distance = point1.dist(point2)
print(f"The distance between the points is: {distance}")