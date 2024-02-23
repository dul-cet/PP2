# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

str1 = re.compile(r'a.*b$')

def match_string(text):
    return str1.fullmatch(text) is not None

print(match_string("acccb"))  # True
print(match_string("ab"))     # True
print(match_string("aasdf"))  # False
print(match_string("abbbs"))  # False