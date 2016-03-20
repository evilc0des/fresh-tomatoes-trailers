# Fresh Tomatoes Movie Trailers
##### Easy movie trailer viewing website in Python

## QuickStart

Follow these easy steps to set up:

- Install [Python 2.7](https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi)
- Clone the repo: `git clone https://github.com/evilc0des/fresh-tomatoes-trailers.git`

<br>This will get you started in making your own kickass movie trailer viewing website. Follow along:
### Add Movies to your catalog

We have already added some movies but you can add more or change the ones already added.

- Open **entertainment_center.py** and add a movie object as follows

```
deadpool = media.Movie("Deadpool","A former Special Forces operative turned mercenary with accelerated healing powers.",
                       "http://ia.media-imdb.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SX640_SY720_.jpg",
                       "https://www.youtube.com/watch?v=FyKWUTwSYAs", "2016", ["Action", "Thriller", "Comedy"])
```

The format is as follows

```
object_name_ = media.Movie("Movie_Name","Movie_Synopsis",
                       "Movie_Poster_URL",
                       "Movie_Trailer_URL", "Movie_Release_date", ["Genre1", "Genre2", ...])
```

- Add the objects to the **movies** list

```
movies = [deadpool, superman_vs_batman, captain_america, xmen_apocalypse, ninja_turtles, (your_movie_object), ....]
```

Now that the movies are added, time to see them in action..

### Start up the Website

It just a matter of running the module **entertainment_center.py**.

Either you can use run command from your IDE 

or from Command line:

```
python entertainment_center.py
```

### Changing the Page View

If you want to change the layout and view of the page the whole view code is dynamically rendered from **fresh_tomatoes.py**

You can make your changes from there. 

#### Copyright, Ownership, License etc etc...

This is a project submission for Udacity Full-stack Web Developer Nanodegree. The _**fresh_tomatoes.py**_ is obtained from udacity and minor changes are introduced to the views.