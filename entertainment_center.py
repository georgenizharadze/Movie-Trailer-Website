# Import requried modules
import fresh_tomatoes
import media


# Initialize instances of specific movies
fitzcarraldo = media.Movie("Fitzcarraldo",
                           "http://www.impawards.com/1982/posters/fitzcarraldo.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=gqugru2d1h8")


nosferatu = media.Movie("Nosferatu the Vampyre",
                        "https://polishpostershop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/k/a/kaja-poster04482.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=S1Rachk7ipI")


aguirre = media.Movie("Aguirre, the Wrath of \nGod",
                      "http://www.impawards.com/1972/posters/aguirre_wrath_of_god_ver2.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=eJDuicFyJPg")


bad_lieutenant = media.Movie("Bad Lieutenant",
                             "http://www.impawards.com/2009/posters/bad_lieutenant_port_of_call_new_orleans_xlg.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=rvy1qlbh5Q4")


my_son = media.Movie("My Son, My Son",
                     "http://www.impawards.com/2009/posters/my_son_my_son_what_have_ye_done.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=nqVbo0GX07M")


queen_of_desert = media.Movie("Queen of the Desert",
                               "http://www.impawards.com/2015/posters/queen_of_the_desert.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=5g2bBX_stcg")


# Create a list of movie instances
movies = [fitzcarraldo, nosferatu, aguirre, bad_lieutenant, my_son,
          queen_of_desert]


def main():
    """Create an html file with movies and serve it via the 'file' protocol"""

    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
