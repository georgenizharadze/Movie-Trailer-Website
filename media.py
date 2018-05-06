class Movie(object):
    """A class with basic information for a movining picture.

    Attributes:
        title: A string containing movie title
        poster_image_url: a string containing poster image url
    trailer_youtube_url: a string containing youtube trailer url
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
