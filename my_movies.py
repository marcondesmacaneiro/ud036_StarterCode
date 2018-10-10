import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/" +
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

star_wars = media.Movie("Star Wars",
                        "The Force Awakens",
                        "https://upload.wikimedia.org/wikipedia/pt/a/ae/" +
                        "Starwars_06.jpg",
                        "https://www.youtube.com/watch?v=4r0287tUEgk")

captain_marvel = media.Movie("Captain Marvel",
                             "Is an upcoming American superhero film based " +
                             "on the Marvel Comics.",
                             "https://upload.wikimedia.org/wikipedia/en/8/" +
                             "85/Captain_Marvel_poster.jpg",
                             "https://www.youtube.com/watch?v=Z1BCujX3pw8")

venom = media.Movie("Venom",
                    " In Venom, journalist Brock gains superpowers after " +
                    "being bound to an alien symbiote whose species plans " +
                    "to invade Earth",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcRvT1RlWWfdC" +
                    "EOyeF00_yBwYzSg4_Nm9oWPNfRMJGviWb6hnLLW",
                    "https://www.youtube.com/watch?v=sVjQw8M_FSM")

movies = [avatar, star_wars, captain_marvel, venom]
fresh_tomatoes.open_movies_page(movies)
