import media

toy_story = media.Movie("Toy Story", 
    "A history of a boy who his imagination run wild",
    "https://es.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.svg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
    "A marine who walks through the jungle",
    "https://es.wikipedia.org/wiki/Avatar_(pel%C3%ADcula)#/media/File:Avatar-Logo-avatar.svg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

interstellar = media.Movie("Interstellar",
    "a multi dimension future collapse into enviromental issues",
    "https://en.wikipedia.org/wiki/Interstellar_(film)#/media/File:Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=1weAVdHUNlk") 

interstellar.show_trailer()