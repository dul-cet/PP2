"""
5. Write a function that takes a category and computes the average IMDB score.
"""

from Dictionary_of_movies import movies

def average_imdb_score_by_category(category):
    movies_by_category = [movie for movie in movies if movie["category"] == category]
    return average_imdb(movies_by_category)

def average_imdb(movies):
    total = 0
    num = 0
    for movie in movies:
        total += movie["imdb"]
        num += 1
    return total / num

category = input()
average_imdb = average_imdb_score_by_category(category)
print(average_imdb)