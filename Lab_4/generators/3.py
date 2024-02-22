# 3. Define a function with a generator which can iterate the numbers,
# which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by_3_and_4_generator(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter the n: "))

divisible_nums = divisible_by_3_and_4_generator(n)
for num in divisible_nums:
    print(num, end=", ")