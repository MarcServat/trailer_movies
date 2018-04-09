import media
import movies

irreversible = media.Movie("Irrversible", 
    "Sex and violence, HOT topic",
    "http://www.fotogramas.es/var/ezflow_site/storage/images/peliculas/irreversible/110105-1-esl-ES/Irreversible1_cartel.jpg",
    "https://www.youtube.com/watch?v=j7EDpDba8bU")

requiem = media.Movie("Requiem",
    "American psychological drama",
    "https://pics.filmaffinity.com/requiem_for_a_dream-174867645-large.jpg",
    "https://www.youtube.com/watch?v=0nU7dC9bIDg")

apocalypto = media.Movie("Apocalypto",
    "As the Mayan kingdom faces its decline, a young man is taken on a perilous journey to a world ruled by fear and oppression.",
    "https://ia.media-imdb.com/images/M/MV5BMzhmNGMzMDMtZDM0Yi00MmVmLWExYjAtZDhjZjcxZDM0MzJhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=ngWBddVNVZs") 

movies_list = [irreversible, requiem, apocalypto]

movies.open_movies_page(movies_list)