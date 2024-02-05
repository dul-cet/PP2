"""
8. Write a function that takes in a list of integers and returns True if it contains `007` in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(nums):
    zero = False
    double_zero = False
    
    for num in nums:
        if num == 0 and not zero:
            zero = True
        elif num == 0 and zero and not double_zero:
            double_zero = True
        elif num == 7 and zero and double_zero:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))   #True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))   #True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))   #False