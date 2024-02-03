"""
5. Write a function that accepts string from user and print all permutations of that string."""

from itertools import permutations

def print_permutations(s):
    all_permutations = permutations(s)
    for perm in all_permutations:
        print(''.join(perm))

input = input()
print_permutations(input)