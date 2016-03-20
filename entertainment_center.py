import media
import fresh_tomatoes

# The movie objects are constructed taking all the properties as its parameters
deadpool = media.Movie("Deadpool",
                       "A former Special Forces operative turned mercenary with accelerated healing powers.",
                       "http://ia.media-imdb.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=FyKWUTwSYAs",
                       "2016", ["Action", "Thriller", "Comedy"])

superman_vs_batman = media.Movie("Batman v Superman: Dawn of Justice",
                                 "Fearing the actions of Superman are left unchecked, Batman takes on the man of steel",
                                 "http://ia.media-imdb.com/images/M/MV5BNTE5NzU3MTYzOF5BMl5BanBnXkFtZTgwNTM5NjQxODE@._V1_SX640_SY720_.jpg",
                                 "https://www.youtube.com/watch?v=eX_iASz1Si8",
                                 "2016", ["Action", "Thriller"])

captain_america = media.Movie("Captain America: Civil War",
                              "Political interference causes a rift between former allies Captain America and Iron Man.",
                              "http://ia.media-imdb.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SX640_SY720_.jpg",
                              "https://www.youtube.com/watch?v=dKrVegVI0Us",
                              "2016", ["Action", "Thriller"])

xmen_apocalypse = media.Movie("X-Men: Apocalypse",
                              "With the emergence of the world's first mutant, Apocalypse, the X-Men unite to defeat his extinction plan.",
                              "http://ia.media-imdb.com/images/M/MV5BMjQxMjY5MzU1NV5BMl5BanBnXkFtZTgwNzgyNjY0NzE@._V1__SX640_SY720_.jpg",
                              "https://www.youtube.com/watch?v=PfBVIHgQbYk",
                              "2016", ["Action", "Thriller", "Adventure"])

ninja_turtles = media.Movie("Teenage Mutant Ninja Turtles: Out of the Shadows",
                            "The Turtles return to save the city from a dangerous threat.",
                            "http://ia.media-imdb.com/images/M/MV5BMjAzODQyNDQxOV5BMl5BanBnXkFtZTgwMjYxMzUwODE@._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=HeaugHGd1Kw",
                            "2016", ["Action", "Adventure", "Comedy"])


# A list of all the movie objects
movies = [deadpool, superman_vs_batman, captain_america, xmen_apocalypse, ninja_turtles]

fresh_tomatoes.open_movies_page(movies)