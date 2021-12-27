import sqlite3
import os

def check_database_exist():

    db_name = 'movie.db'
    os.chdir('database')
    if db_name in os.listdir():
        return True
    else:
        return False

class moviedb:

    def __init__(self):
        conn = sqlite3.connect('movie.db')
        c = conn.cursor()
        c.execute('''
        create table if not exists user 
        ([user_id] text PRIMARY KEY, [user_name] text, 
        [user_email] text UNIQUE , [user_age] int, [user_gender] text)
        ''')
        c.execute('''
        create table if not exists movie
        ([movie_id] text PRIMARY KEY, [movie_name] text,
        [movie_genre] text, [movie_description] text, [movie_director] text,
        [movie_actors] text, [movie_language] text, [movie_category] text)
        ''')
        c.execute('''
        create table if not exists moviestatus
        ([status_id] text PRIMARY KEY, [user_id] text,
        [movie_id] text, [is_liked] int)
        ''')
        c.execute('''
        create table if not exists logrequest
        ([start_time] text, [stop_time] text, 
        [execution_id] text PRIMARY KEY, 
        [executed_by] text, [function_params] text,
        [response_status] text, [response_msg] text)
        ''')
        c.execute('''
        create table if not exists logprogress
        ([execution_id] text PRIMARY KEY, [progress_msg] text)
        ''')
        c.execute('''
        create table if not exists logerror
        ([execution_id] text PRIMARY KEY, [error_msg] text)
        ''')
        conn.commit()
        c.close()
        conn.close()



