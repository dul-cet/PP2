"""
4. Write a function that takes a list of movies and computes the average IMDB score.
"""

from Dictionary_of_movies import movies

def average_imdb(movies):
    total = 0
    num = 0
    for movie in movies:
        total += movie["imdb"]
        num += 1
    return total / num

average_imdb_score = average_imdb(movies)
print(average_imdb_score)