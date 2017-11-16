
from media import Movie
from fresh_tomatoes import *

def createMovies():

    movie1 = Movie()
    movie1.trailer_url = "https://v.youku.com/v_show/id_XMzE1NzYzMTg1Mg==.html"
    movie1.title = "HeadHunter"
    movie1.poster_image_url = "https://vthumb.ykimg.com/vi/XMzE1NzYzMTg1Mg==/89/default.jpg"

    movie2 = Movie()
    movie2.trailer_url = "https://v.youku.com/v_show/id_XMzE1OTA2NjI4OA==.html"
    movie2.title = "chenqiaoen"
    movie2.poster_image_url = "https://vthumb.ykimg.com/vi/XMzE1OTA2NjI4OA==/89/default.jpg"

    movies = [movie1, movie2]

    return movies

movieInfo = createMovies()

# for movie in movieInfo:
#     print movie.description()

# content = create_movie_tiles_content(movieInfo)

# print content

open_movies_page(movieInfo)
