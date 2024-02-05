"""
1. Write a function that takes a single movie and returns `True` if its IMDB score is above 5.5
"""

from Dictionary_of_movies import movies

def is_movie_above_5_5(name):
    for movie in movies:
        if movie["name"] == name:
            return movie["imdb"] > 5.5
    return False

name = input()
if is_movie_above_5_5(name):
    print("True")
else:
    print("False")