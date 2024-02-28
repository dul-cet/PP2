# 4. Write a Python program that invoke square root function after specific milliseconds. 
"""
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
"""

import time

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return number ** 0.5

number = int(input("Enter a number: "))
milliseconds = int(input("Enter milliseconds: "))
result = square_root_after_milliseconds(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")