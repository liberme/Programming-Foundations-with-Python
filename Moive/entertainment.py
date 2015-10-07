import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of toy and boy",
                        "http://uploads.neatorama.com/wp-content/uploads/2010/07/poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marin on an alien planet",
                     "http://www.1234plus.com/wp-content/uploads/2010/02/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

big_hero_6 = media.Movie("Big Hero 6",
                         "A boy with his brother's roboter",
                         "http://img3.wikia.nocookie.net/__cb20140911121002/disney/images/8/89/Big_Hero_6_film_poster.jpg",
                         "https://www.youtube.com/watch?v=lVFDDcQHZYo")

minions = media.Movie("Minious",
                      "A story of minions",
                      "http://o.aolcdn.com/hss/storage/midas/b5236e4ccc84ef48ef5993b2af8e4010/202267673/minions_2015-wide.jpg",
                      "https://www.youtube.com/watch?v=Ja-vnNquM-8")

conan = media.Movie("Detective Conan: Sunflowers of Infemo",
                    "A kid who always bring dead",
                    "http://i.gbc.tw/gb_img/3402644.jpg",
                    "https://www.youtube.com/watch?v=54iAmrSTkEg")


ant_man = media.Movie("Ant Man",
                      "A man only ant size",
                      "http://parksandresorts.wdpromedia.com/media/disneyparks/blog/wp-content/uploads/2015/06/tuytuy736882.jpg",
                      "www.youtube.com/watch?v=KX5-nr2Ms8I")

movies = [toy_story, avatar, big_hero_6, minions, conan, ant_man]
fresh_tomatoes.open_movies_page(movies)
