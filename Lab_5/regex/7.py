# 7. Write a python program to convert snake case string to camel case string.

import re

def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))

print(snake_to_camel("hello_world"))  # HelloWorld
print(snake_to_camel("seventeen_bts"))  # SeventeenBts