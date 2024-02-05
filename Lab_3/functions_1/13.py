"""
13. Write a program able to play the `"Guess the number"` - game,
where the number to be guessed is randomly chosen between 1 and 20.
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_n = random.randint(1, 20)
    guess_done = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guess_done += 1

        if guess < secret_n:
            print("Your guess is too low.")
        elif guess > secret_n:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guess_done} guesses!")
            break

guess_the_number()