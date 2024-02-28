# 1. Write a Python program with builtin function to multiply all the numbers in a list

import math

my_list = [int(x) for x in input("Enter numbers: ").split()]

result = math.prod(my_list)
print(result)