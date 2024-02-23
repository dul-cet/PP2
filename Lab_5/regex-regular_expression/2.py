# 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

str1 = re.compile(r'ab{2,3}')

def match_string(text):
    return str1.fullmatch(text) is not None

print(match_string("abb"))    # True
print(match_string("abbb"))   # True
print(match_string("abbbb"))  # False
print(match_string("ac"))     # False