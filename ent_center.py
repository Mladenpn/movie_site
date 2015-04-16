import media
import fresh_tomatoes

ocean12 = media.Movie("Ocean12", "","http://upload.wikimedia.org/wikipedia/sr/thumb/0/01/Ousnovih_12.jpg/250px-Ousnovih_12.jpg", "https://www.youtube.com/watch?v=TSKzL-8RHuw")


T2 = media.Movie("T2", "","http://images2.fanpop.com/image/photos/11600000/T2-terminator-11685785-1000-1500.jpg","https://www.youtube.com/watch?v=DxgLwrW9h_A")


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

