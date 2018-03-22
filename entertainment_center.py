import fresh_tomatoes
'''fresh_tomatoes python file contains the codings for creation of webpage. '''
import media
'''media is file which contains class file in it'''

american_made = media.Movie("American Made","Doug Liman","29/09/2017","https://upload.wikimedia.org/wikipedia/en/c/ca/American_Made_%28film%29.jpg","https://youtu.be/AEBIJRAkujM")

blade_runner = media.Movie("Blade Runner","Ridley Scott","25/06/1982","https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg","https://youtu.be/gCcx85zbxz4")

kingsman = media.Movie("Kingsman","Matthew Vaughn","13/02/2015","https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg","https://youtu.be/0fvqnGmr9S8")

sully = media.Movie("Sully","Clint Eastwood","09/09/2016","https://upload.wikimedia.org/wikipedia/en/8/82/Sully_xxlg.jpeg","https://youtu.be/mjKEXxO2KNE")

dunkirk = media.Movie("Dunkirk","Christopher Nolan","13/07/2017","https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg","https://youtu.be/F-eMt3SrfFU")

the_lego_ninjago_movie = media.Movie("The Lego Ninjago Movie","Charlie Bean","22/09/2017","https://upload.wikimedia.org/wikipedia/en/9/9f/The_Lego_Ninjago_Movie.jpg","https://youtu.be/VJBS1ogEVHE")

''' Movie class which is in media file is called by passing the arguments such as
1.Movie name
2.Screenwriter
3.Launch Date
4.Poster Image
5.Trailer URL
and it is stored in appropriate objects.'''

films=[american_made,blade_runner,kingsman,sully,dunkirk,the_lego_ninjago_movie]
'''movie names are created in a list so as to access easy'''
fresh_tomatoes.open_movies_page(films)
