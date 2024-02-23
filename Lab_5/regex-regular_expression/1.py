# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

str1 = re.compile(r'ab*')

def match_string(text):
    return str1.fullmatch(text) is not None

print(match_string("a"))   # True
print(match_string("ab"))  # True
print(match_string("abb")) # True
print(match_string("ac"))  # False