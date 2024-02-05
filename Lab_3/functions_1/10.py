"""
10. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection `set`.
"""

def unique(lst):
    ulst = []
    
    for element in lst:
        if element not in ulst:
            ulst.append(element)
    
    return ulst
    
nums = input()
lst = [int(num) for num in nums.split()]
result = unique(lst)

print(lst)
print(result)