"""
json library training
>>> import sys; sys.tracebacklimit = 0
>>> dump_movies(movie_dict)
>>> print(load_movies() == movie_dict)
True
"""

import json

movie_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
    {
      "title": "Parasite",
      "director": "Bong Joon Ho",
      "year": 2019
    }
  ]
}

def dump_movies(movies):
    with open("movies.json", "w") as json_file:
        json.dump(movies, json_file, indent=4)


def load_movies():
    with open("movies.json") as json_file:
        movie_dict_from_json = json.load(json_file)
    return movie_dict_from_json