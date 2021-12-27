from entity_layer.movie import Movie
import sqlite3

class MovieStorage():

    def __init__(self):
        self.conn = sqlite3.connect('movie.db')
        self.c = self.conn.cursor()


    def save_movie(self,movie:Movie):
        movie_id = str(movie.movie_id)
        movie_name = movie.movie_name
        movie_genre = movie.movie_genre
        movie_description = movie.movie_description
        movie_director = movie.movie_director
        movie_actors = movie.movie_actors
        movie_language = movie.movie_language
        movie_category = movie.movie_category

        query = "insert or ignore into movie values(?, ?, ?, ?, ?, ?, ?, ?);"
        self.c.execute(query,(movie_id, movie_name, movie_genre, movie_description, movie_director, movie_actors, movie_language, movie_category))
        self.conn.commit()
        if(self.c.execute(query,(movie_id, movie_name, movie_genre, movie_description, movie_director, movie_actors, movie_language, movie_category))):
            return True
        else:
            return False


    def get_movie(self,email_id) -> Movie:
        pass
