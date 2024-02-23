# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

str1 = re.compile(r'[ ,.]')

def replace_characters(text):
    return str1.sub(':', text)

print(replace_characters("Fallin' flower, Bittersweet are masterpieces."))  
# Fallin':flower::Bittersweet:are:masterpieces: