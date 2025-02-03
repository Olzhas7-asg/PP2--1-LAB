
import random
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Function to check if a movie has an IMDB score above 5.5
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

# 2. Function to get movies with an IMDB score above 5.5
def highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

# 3. Function to get movies by category
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

# 4. Function to compute the average IMDB score of a list of movies
def average_imdb(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

# 5. Function to compute the average IMDB score of movies in a given category
def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)

random_movie = random.choice(movies)
random_category = random.choice([movie["category"] for movie in movies])
print(f"1. Is '{random_movie['name']}' highly rated?", is_highly_rated(random_movie))
print("2. Random Highly rated movies:", highly_rated_movies(movies))
print(f"3. Movies in random category '{random_category}':", movies_by_category(movies, random_category))
print("4. Average IMDB score of all movies:", average_imdb(movies))
print(f"5. Average IMDB score of '{random_category}' category:", average_imdb_by_category(movies, random_category))