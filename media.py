#!/usr/bin/env python
# coding: utf-8


class Movie():
    """This class is a way to store all about one movie information."""
#    Funcao que inicia a classe com suas variaveis
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
