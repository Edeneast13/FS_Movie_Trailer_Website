import webbrowser


"""
Module to display movie object, attributes and instances
"""


class Movie():
    """
    Class object stores movie related information
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        initialize instance of class Movie

        :param movie_title: title
        :param poster_image_url: poster_image_url
        :param trailer_youtube_url: trailer_youtube_url
         """

        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        