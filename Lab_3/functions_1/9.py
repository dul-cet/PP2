"""
9. Write a function that computes the volume of a sphere given its radius.
"""

import math
def v(r):
    v = (4/3) * math.pi * r**3
    return v
    
r=int(input())
result = v(r)
print(result)