'''
{
 'name': 'The Matrix',黑客帝国
 'director': 'Wachowskis',
 'year': '1994'
}

First, the application must allow to add new movies to the collection;
• The application must allow users to view all the movies in their collection;
• The application must also allow users to find any particular movie by any of its attributes (more info in the next page...)
'''

import sqlite3

def connection():

    conn = sqlite3.connect("movie.db")
    c = conn.cursor()
#    c.execute("drop table if exists my_movie_table")
    c.execute("create table if not exists my_movie_table (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT ,director TEXT,year INTEGER)")
    conn.commit()
    c.close()

def save_to_db(title,director,year):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()

    if title and director and year:

        title=str(title)
        director=str(director)
        year=int(year)

        c.execute("insert into my_movie_table (title,director,year) values(?,?,?)",(title,director,year))
        conn.commit()
    c.close()

def delete_movie(id):
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()
   # print (type(id))
    c.execute("delete from my_movie_table where id=?",(id,))
    conn.commit()
    c.close()

def view_all():
    conn = sqlite3.connect("movie.db")
    c = conn.cursor()
    c.execute("SELECT * FROM my_movie_table")
    result = c.fetchall()
    c.close()
    return result

def search(title="",director="",year=""):
    conn=sqlite3.connect("movie.db")
    c=conn.cursor()
    if not title and not director and not year:
        view_all()
    else:
        c.execute("select * from my_movie_table where title=? or director =? or year=?",(title,director,year))
        result= c.fetchall()
        c.close()
        return result


