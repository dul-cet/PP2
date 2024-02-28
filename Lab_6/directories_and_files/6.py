# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

def generate_text_files():
    alphabet = string.ascii_uppercase
    for letter in alphabet:
        file_name = letter + '.txt'
        with open(file_name, 'w') as file:
            pass

generate_text_files()