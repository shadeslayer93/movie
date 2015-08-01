import fresh_tomatoes
import media

spectre = media.Movie("Spectre", "https://www.youtube.com/watch?v=l9hMaqdNzz8", "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg", "The story revealing the dark past of the world's most famous spy, James Bond ")

the_girl_with_the_dragon_tatoo = media.Movie("The Girl with the Dragon Tatoo", "https://www.youtube.com/watch?v=WVLvMg62RPA", "https://upload.wikimedia.org/wikipedia/en/8/80/The_Girl_with_the_Dragon_Tattoo_Poster.jpg", "This thriller by David Fincher, revolves around the story of a missing girl, coupled with the genius of a Hacker and a journalist trying to uncover it.")

the_social_network = media.Movie("The Social Network", "https://www.youtube.com/watch?v=lB95KLmpLR4", "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg", "The story of the world's youngest billionaire, Mark Zuckerberg. This story shows his rise, that comes at a cost of friendship embroiled with legal battles.")

up = media.Movie("Up", "https://www.youtube.com/watch?v=pkqzFUhGPJg","https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg","A beautiful story about Adventure and Love!!")

the_theory_of_everything = media.Movie("The Theory of Everything", "https://www.youtube.com/watch?v=Salz7uGp72c", "https://upload.wikimedia.org/wikipedia/en/b/b8/Theory_of_Everything.jpg", "The story of one of the greatest mings of the 21st century !!")

the_karate_kid = media.Movie("The Karate Kid", "https://www.youtube.com/watch?v=2SmmxvHLsKk", "https://upload.wikimedia.org/wikipedia/en/d/d5/Karate_kid_ver2.jpg", "The story of the original Karate Kid, retold in a different place, in a different time. A story of Honour, Bravery & Courage.")

blood_diamond = media.Movie("Blood Diamond", "https://www.youtube.com/watch?v=yknIZsvQjG4", "https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg", "Blood Diamond is a 2006 American-German political war thriller film.The title refers to blood diamonds, which are diamonds mined in war zones and sold to finance conflicts, and thereby profit warlords and diamond companies across the world.")

about_time = media.Movie("About Time", "https://www.youtube.com/watch?v=7OIFdWk83no", "https://upload.wikimedia.org/wikipedia/en/8/88/About_Time_Poster.jpg", "About Time is a 2013 British romantic comedy-drama film about a young man with the special ability to time travel who tries to change his past in order to improve his future.")

the_dark_knight = media.Movie("The Dark Knight", "https://www.youtube.com/watch?v=EXeTwQWrcwY", "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", "This epic movie, takes a dark look at one of the greatest comic heroes and his batlles with his arch villain. Great direction as always, by the one and only, Christopher Nolan.")

movies = [spectre, the_girl_with_the_dragon_tatoo, the_social_network,up, the_theory_of_everything, the_karate_kid, blood_diamond, about_time, the_dark_knight ]

fresh_tomatoes.open_movies_page(movies)

