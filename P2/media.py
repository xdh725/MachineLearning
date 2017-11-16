# -*- coding: UTF-8 -*-

# 电影信息对象类
class Movie(object):
    """docstring for Movie."""

    #类初始化 并对三个成员变量赋值 预设默认值
    def __init__(self, title='UnkownMovie', poster_image_url='', trailer_url=''):
        super(Movie, self).__init__()
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

    #测试用 打印类的成员变量信息
    def description(self):
        print('title: ' + self.title + '\nposter_image_url: ' + self.poster_image_url + '\ntrailer_url:' + self.trailer_url)
        pass

# movie = Movie()

# movie.movie_title = "HeadHunter"
# movie.poster_image_url = "https://vthumb.ykimg.com/vi/XMzE1NzYzMTg1Mg==/89/default.jpg"
# movie.trailer_url = "https://v.youku.com/v_show/id_XMzE1NzYzMTg1Mg==.html"

# movie.description()
