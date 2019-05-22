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

conn = sqlite3.connect("movie.db")
c = conn.cursor()

def save_to_db(movie):

    c.execute("insert into movie_table values(?,?,?)",(movie["title"],movie["director"],movie["year"]))
    conn.commit()

def read_from_db():
    movielist=[]
    for record in c.execute("SELECT * FROM movie_table"):
        movielist.append({"title":record[0],"director":record[1],"year":record[2]})

    return movielist
def show_movies(movie_list):
    for movie in movie_list:
        print("title: {}; director: {} ; year:{} :".format((movie["title"]), movie["director"],
                                                           movie["year"]))
def movie_collection():
    movielist= []
    result =[]
    # read movielist from file :
    movielist=read_from_db()
    # ask for selection:
    # 1 --list all
    # 2---search
    while True:
        try:

            selection = int (input("please input your selection 1--for list all nmovies; 2--for search movies; 3--for new movie input 4--exit"))
            if selection ==1:
                if (len(movielist)==0):
                    print ("no movie ")
                    continue
                show_movies(movielist)

            if selection ==3:

                title =  input("input movie title ")
                director = input("input director")
                year = int(input("input the year"))

                for movie in movielist:
                    if movie["title"]==title:
                        print ("movie title exists already")
                        break
                else:
                    movielist.append({"title": title, "director": director, "year": year})
                    save_to_db({"title": title, "director": director, "year": year})

            if selection ==2:
                search_by = input ("input the movie proerty to search by entering 'tilte' or 'director' or 'year' ")
                condition = input ("input the movie detail you specify as title or director or year")
                if not search_by in ['title','director','year']:
                    print ("select key word incorrect, would back to main menu ")
                    continue
                if search_by =='year' :
                    year = int(condition)

                for movie in movielist:
                    if(movie[search_by]==condition):
                        result.append (movie)
                if result :
                    show_movies(result)


            if selection==4:
                break
        except Exception:
            print (Exception.with_traceback())


movie_collection()
conn.close()
