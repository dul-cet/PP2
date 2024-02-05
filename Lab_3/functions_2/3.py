"""
3. Write a function that takes a category name and returns just those movies under that category.
"""

from Dictionary_of_movies import movies

def movies_category(category):
    return [movie for movie in movies if movie["category"] == category]

category = input()
movies_by_category = movies_category(category)

if movies_by_category:
    for movie in movies_by_category:
        print(f"{movie['name']}")
else:
    print(f"There is no movie in this category.")