def is_palindrome():
    word = input().lower().replace(' ', '')
    reversed_word = word[::-1]
    if word == reversed_word:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")

is_palindrome()