# 9. Write a Python program to insert spaces between words starting with capital letters.

import re

str1 = re.compile(r'(?<!^)(?=[A-Z])')

def insert_spaces(text):
    return str1.sub(' ', text)

print(insert_spaces("SeventeenBtsStrayKids"))  
# Seventeen Bts Stray Kids