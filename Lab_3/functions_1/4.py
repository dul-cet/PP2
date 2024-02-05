"""
4. You are given list of numbers separated by spaces.
Write a function `filter_prime` which will take list of numbers as an agrument
and returns only prime numbers from the list.
"""

def is_prime(n):
    if n == 0:
        return False
    if n < 0:
        n = -n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = list(map(int, input().split()))
print(lst)

prime_numbers = [item for item in lst if is_prime(item)]
print(prime_numbers)