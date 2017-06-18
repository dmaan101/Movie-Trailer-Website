import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","Story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar","Marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)

#avatar.show_trailer()
shawshank_redemption = media.Movie("Shawshank Redemption","Story of a great escape plan","https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

pursuit_of_happyness = media.Movie("The Pursuit of Happyness","The Pursuit of Happyness is a 2006 American biographical drama film based on entrepreneur Chris Gardner's nearly one-year struggle being homeless.","https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg","https://www.youtube.com/watch?v=zF4EDt5kJqY")

southpaw = media.Movie("Southpaw"," The film follows a young boxer who sets out to get his life back on track after losing his wife in an accident and his young daughter to protective services.","https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg","https://www.youtube.com/watch?v=Mh2ebPxhoLs")

blood_diamond = media.Movie("Blood Diamond","The title refers to blood diamonds, which are diamonds mined in war zones and sold to finance conflicts, and thereby profit warlords and diamond companies across the world.","https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg","https://www.youtube.com/watch?v=XtPX2kXhu7I")

movies = [toy_story,avatar,shawshank_redemption,pursuit_of_happyness,southpaw,blood_diamond]
fresh_tomatoes.open_movies_page(movies)
