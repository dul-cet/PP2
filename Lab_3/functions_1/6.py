"""
6. Write a function that accepts string from user, return a sentence with the words reversed.
`We are ready -> ready are We`
"""

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input = input("Enter a sentence: ")
result = reverse_words(input)
print(result)