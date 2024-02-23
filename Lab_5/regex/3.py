# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

str1 = re.compile(r'[a-z]+_[a-z]+')

def find_sequences(text):
    return str1.findall(text)

print(find_sequences("hello_world and 17Sseventeen_bts"))  
# ['hello_world', 'seventeen_bts']