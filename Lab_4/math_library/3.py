"""
3. Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""

import math

num_sides = int(input("Number of sides: "))
side_length = int(input("Length of a side: "))

area = int((num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides)))
print(area)