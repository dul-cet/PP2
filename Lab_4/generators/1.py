# 1. Create a generator that generates the squares of numbers up to some number N.

def squares_generator(N):
    for i in range(1, N):
        yield i**2

N = int(input("Enter the n: "))

squares = squares_generator(N)
for square in squares:
    print(square)