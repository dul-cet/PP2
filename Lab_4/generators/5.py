# 5. Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter the n: "))

for num in countdown(n):
    print(num)