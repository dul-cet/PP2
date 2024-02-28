# 2. Write a Python program with builtin function that accepts a string
# and calculate the number of upper case letters and lower case letters

def up_low(strng):
    global u, l
    for i in strng:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1

u = 0
l = 0
n=input()

up_low(n)
print("upper case:", u)
print("lower case:", l)