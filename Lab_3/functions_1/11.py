"""
11. Write a Python function that checks whether a word or phrase is `palindrome` or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""

def is_palindrome():
    word = input().lower().replace(' ', '')
    reversed_word = word[::-1]
    if word == reversed_word:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")

is_palindrome()