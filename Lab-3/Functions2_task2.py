import json_exer
def subListAbove5p5(movies):
    subList = []
    for movie in movies:
        if movie["imdb"] < 5.5:
            subList.append(movie)
    return subList

def connection():
    with open("data.json", "r") as file:
        movies = json.load(file)
        moviesList = movies["movies"]
        file.close()
    return moviesList

# movies = [
#     {
#         "name": "Usual Suspects",
#         "imdb": 7.0,
#         "category": "Thriller"
#     },
#     {
#         "name": "Hitman",
#         "imdb": 6.3,
#         "category": "Action"
#     },
#     {
#         "name": "Dark Knight",
#         "imdb": 9.0,
#         "category": "Adventure"
#     },
#     {
#         "name": "The Help",
#         "imdb": 8.0,
#         "category": "Drama"
#     },
#     {
#         "name": "The Choice",
#         "imdb": 6.2,
#         "category": "Romance"
#     },
#     {
#         "name": "Colonia",
#         "imdb": 7.4,
#         "category": "Romance"
#     },
#     {
#         "name": "Love",
#         "imdb": 6.0,
#         "category": "Romance"
#     },
#     {
#         "name": "Bride Wars",
#         "imdb": 5.4,
#         "category": "Romance"
#     },
#     {
#         "name": "AlphaJet",
#         "imdb": 3.2,
#         "category": "War"
#     },
#     {
#         "name": "Ringing Crime",
#         "imdb": 4.0,
#         "category": "Crime"
#     },
#     {
#         "name": "Joking muck",
#         "imdb": 7.2,
#         "category": "Comedy"
#     },
#     {
#         "name": "What is the name",
#         "imdb": 9.2,
#         "category": "Suspense"
#     },
#     {
#         "name": "Detective",
#         "imdb": 7.0,
#         "category": "Suspense"
#     },
#     {
#         "name": "Exam",
#         "imdb": 4.2,
#         "category": "Thriller"
#     },
#     {
#         "name": "We Two",
#         "imdb": 7.2,
#         "category": "Romance"
#     }
# ]
movies = connection()
print(subListAbove5p5(movies))