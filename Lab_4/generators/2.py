# 2. Write a program using generator to print the even numbers between 0 and 
# n in comma separated form where n is input from console.

def even_numbers_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter the n: "))

even_numbers = even_numbers_generator(n)
for num in even_numbers:
    print(num, end=", ")