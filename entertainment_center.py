# coding=utf-8
import fresh_tomatoes
import media

spiderman_Into_The_Spiderverse= media.Movie("Spiderman Into The Spiderverse",
"a story about a boy that becomes spiderman",
"https://upload.wikimedia.org/wikipedia/en/b/b8/Spider-Man_Into_the_Spider-Verse_%282018_poster%29.png",
"https://www.youtube.com/watch?v=g4Hbz2jLxvQ")

# spiderman_Into_The_Spiderverse.show_trailer()
# spiderman_Into_The_Spiderverse.show_image()



detective_Pikachu = media.Movie("Pokemon: Detective Pikachu",
 "About a pokemon",
 "https://upload.wikimedia.org/wikipedia/en/e/e5/Pokémon_Detective_Pikachu_teaser_poster.jpg",
 "https://www.youtube.com/watch?v=1roy4o4tqQM")

death_Note = media.Movie("Death Note",
"A high school student discovers a supernatural notebook that has deadly powers",
"https://upload.wikimedia.org/wikipedia/en/6/6f/Death_Note_Vol_1.jpg",
"https://www.youtube.com/watch?v=gTLnDIeSZr8")

movies=[spiderman_Into_The_Spiderverse,detective_Pikachu,death_Note]
fresh_tomatoes.open_movies_page(movies)
