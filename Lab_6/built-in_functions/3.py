# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.

string_to_check = input()

if string_to_check == string_to_check[::-1]:
    print("palindrome")
else:
    print("not palindrome")