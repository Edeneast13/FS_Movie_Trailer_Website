import fresh_tomatoes
import media


#three movie objects each containing the title, poster url , and trailer url
fast_and_furious = media.Movie(
        "The Fast & The Furious",
        "https://image.tmdb.org/t/p/original/j9jeJyXWdx1eGVRRwA1drTEjCyV.jpg",
        "https://www.youtube.com/watch?v=ZsJz2TJAPjw")

return_of_the_jedi = media.Movie(
        "Star Wars: The Return Of The Jedi",
        "https://image.tmdb.org/t/p/original/tDI5QBosczWGj6w1Xp0Uidr6GKW.jpg",
        "https://www.youtube.com/watch?v=7L8p7_SLzvU")

two_towers = media.Movie(
        "The Lord Of The Rings: The Two Towers",
        "https://image.tmdb.org/t/p/original/5o5fv1dHG7vWoH2hmqwihVPBoBm.jpg",
        "https://www.youtube.com/watch?v=2dlRvAjU_RI")

# creates an array of movies containing the 3 created movies
movies = [fast_and_furious, return_of_the_jedi, two_towers]

# passes the created movie object into the open_movies_page function
fresh_tomatoes.open_movies_page(movies)

