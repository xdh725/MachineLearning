# -*- coding: UTF-8 -*-

from media import Movie
from fresh_tomatoes import *

# 方法体 创建并返回包含两个电影对象的对象数组 
def createMovies():

    #初始化电影对象实例1
    movie1 = Movie()
    movie1.trailer_url = "https://v.youku.com/v_show/id_XMzE1NzYzMTg1Mg==.html"
    movie1.title = "HeadHunting"
    movie1.poster_image_url = "https://vthumb.ykimg.com/vi/XMzE1NzYzMTg1Mg==/89/default.jpg"

    #初始化电影对象实例2
    movie2 = Movie()
    movie2.trailer_url = "https://v.youku.com/v_show/id_XMzE1OTA2NjI4OA==.html"
    movie2.title = "chenqiaoen"
    movie2.poster_image_url = "https://vthumb.ykimg.com/vi/XMzE1OTA2NjI4OA==/89/default.jpg"

    #初始化一个电影对象数组
    movies = [movie1, movie2]

    return movies

#创建包含电影信息的数组
movieInfo = createMovies()

# for movie in movieInfo:
#     print movie.description()

# content = create_movie_tiles_content(movieInfo)

# print content

#将包含电影信息的数组数据传入open_movies_page方法中 先生成一个html文件并打开
open_movies_page(movieInfo)
