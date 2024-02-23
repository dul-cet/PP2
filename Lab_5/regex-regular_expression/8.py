# 8. Write a Python program to split a string at uppercase letters.

import re

str1 = re.compile(r'[A-Z][a-z]*')

def split_at_uppercase(text):
    return str1.findall(text)

print(split_at_uppercase("SeventeenBtsStrayKids"))  
# ['Seventeen', 'Bts', 'Stray', 'Kids']