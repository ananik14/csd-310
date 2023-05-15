# This is a sample Python script.
import JOIN as JOIN

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


    #Execute an inner on all tables
    def show_films(cursor, title ):


    # inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film
INNER JOIN genre ON film.genre_id=genre.genre_id
INNER JOIN studio ON film.studio_id=studio.studio_id);


    # get the results form the cursor object
    films = cursor.fetchall()

        print("\n -- {} --".format(film));

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]));


