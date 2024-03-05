# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

str1 = re.compile(r'[A-Z][a-z]+')

def find_sequences(text):
    return str1.findall(text)

print(find_sequences("Music is perfect"))  
# ['Music']