import uuid

def movie_input():
    print("MOVIE INPUT \n")
    movie_name = input("Movie Name: ")
    movie_genre = input("Movie Genre: ")
    movie_description =input("Movie Description: ")
    movie_director = input("Movie Director: ")
    movie_actors = input("Movie Actors: ")
    movie_language = input("Movie Language: ")
    movie_category = input("Movie Category: ")

    movie_id = uuid.uuid4()

    return movie_id, movie_name, movie_genre, movie_description, movie_director, movie_actors, movie_language, movie_category
