"""
2. Write a function that returns a sublist of movies with an IMDB score above 5.5.
"""

from Dictionary_of_movies import movies

def is_above_5_5(movie):
    return movie["imdb"] > 5.5

movies_above_5_5 = [movie for movie in movies if is_above_5_5(movie)]
print(f"Movies with IMDB rating above 5.5: {[movie['name'] for movie in movies_above_5_5]}")