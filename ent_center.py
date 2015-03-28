import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Prica o decaku i njegovim igrackama koje su ozivele","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar", "Marinac na nepoznatoj planeti","http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print (avatar.storyline)
#avatar.show_trailer()

rocky = media.Movie("Rocky", "Prica o dripcu koji postaje bokser","http://vignette2.wikia.nocookie.net/rocky/images/3/35/Rockynovel.jpg/revision/latest/scale-to-width/250?cb=20080101171536","https://www.youtube.com/watch?v=3VUblDwa648")
#rocky.show_trailer()

zikina_dinastija = media.Movie("Zikina Dinastija","Avanture Zike Pavlovica","http://upload.wikimedia.org/wikipedia/sr/b/b0/Ludegodine.jpg","https://www.youtube.com/watch?v=NXzBfGAUTPo")

tesna_koza = media.Movie("Tesna Koza", "Avanture Sojica i Pantica","http://upload.wikimedia.org/wikipedia/sr/5/51/Tesna_koza_1.jpg","https://www.youtube.com/watch?v=oOmqQEEjNAc")



movies = [toy_story, avatar, rocky, zikina_dinastija, tesna_koza]


#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)

