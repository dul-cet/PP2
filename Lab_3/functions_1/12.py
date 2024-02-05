"""
12. Define a functino `histogram()` that takes a list of integers and prints a histogram to the screen.
For example, `histogram([4, 9, 7])` should print the following:
****
*********
*******
"""

def histogram():
    numbers = list(map(int, input().split()))
    for num in numbers:
        print('*' * num)

histogram()