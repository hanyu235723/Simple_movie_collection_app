
import tkinter as tk
import BackEnd

def seleted_list(event):
    global selected_rows
    selected_rows= movie_list.curselection()
    #currently we only assume to support signle selection
    if selected_rows:
        single_select_row=selected_rows[0]
        movie_selected=movie_list.get(single_select_row)

        title_entry.delete(0,tk.END)
        director_entry.delete(0, tk.END)
        year_entry.delete(0,tk.END)
        title_entry.insert(tk.END,movie_selected[1])
        director_entry.insert(tk.END,movie_selected[2])
        year_entry.insert(tk.END,movie_selected[3])

def get_search_result():
    result=[]
    movie_list.delete(0,tk.END)
    result=BackEnd.search(title_entry.get(), director_entry.get(), year_entry.get())
    if result :
        for movie in result:

            movie_list.insert(tk.END, movie)
    else:
        movie_list.insert(1,"no search result")

def add_new_movie():
    if title_entry or director_entry or year_entry:
        BackEnd.save_to_db(
            title_entry.get(), director_entry.get(), year_entry.get())

def get_all_movies():
    result=[]
    movie_list.delete(0, tk.END)
    result = BackEnd.view_all()
    if result:
        for movie in result:
            movie_list.insert(tk.END, movie)
    else:
        movie_list.insert(1,"no movie to display")

def delete_movie():

    for rowid in selected_rows:
      #  print (movie_list.get(rowid))
        BackEnd.delete_movie(movie_list.get(rowid)[0])

window= tk.Tk()
window.grid_columnconfigure(0,weight=1)

title =tk.Label(window, text="Title")
title.grid(row=0,column=0)

director =tk.Label(window, text="Director")
director.grid(row=1,column=0)

year =tk.Label(window, text="Year")
year.grid(row=2,column=0)

title_entry=tk.Entry(window)
title_entry.grid(row=0,column=1)

director_entry=tk.Entry(window)
director_entry.grid(row=1,column=1)

year_entry=tk.Entry(window)
year_entry.grid(row=2,column=1)

movie_list=tk.Listbox(window, height=6,width=35)
movie_list.bind('<<ListboxSelect>>',seleted_list)
movie_list.grid(row=4,column=0,rowspan=3,columnspan=4)

search_button=tk.Button(window,text="search",width=12,command=get_search_result)
search_button.grid(row=4,column=5)

insert_button=tk.Button(window,text="add new movie",width=12,command=add_new_movie)
insert_button.grid(row=5,column=5)

view_all=tk.Button(window,text="view all",width=12,command=get_all_movies)
view_all.grid(row=6,column=5)

view_all=tk.Button(window,text="delete",width=12,command=delete_movie)
view_all.grid(row=7,column=5)

window.title("movie collector")
window.mainloop()