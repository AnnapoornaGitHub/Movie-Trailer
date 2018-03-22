import webbrowser 

class Movie():
    ''' It has the initialiaze function and show_trailer function.'''
    def __init__(self,movie_title,movie_director,movie_release_date,movie_posterimage,movie_trailer,):
        '''It a constructor and creates space in the memory for instance of the object.
        Inputs are:
        1.movie._title
        2.movie_director
        3.movie_release_date
        4.movie_poster_image
        5.movie_trailer_url
        It will assign the appropriate values to the objects.'''
        self.title = movie_title
        self.director = movie_director
        self.release_date = movie_release_date
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_posterimage

    def show_trailer(self):
        '''It uses the webbrowser function to open the movie trailer webpage. '''
        webbrowser.open(self.trailer)
    
