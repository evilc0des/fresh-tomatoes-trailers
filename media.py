import webbrowser


class Movie:
    # constructor for the movie class takes movie properties as parameter and stores them
    def __init__(self, mov_title, mov_story, mov_poster, mov_trailer, mov_date, mov_genre):
        self.title = mov_title
        self.storyline = mov_story
        self.poster_image_url = mov_poster
        self.trailer_youtube_url = mov_trailer
        self.date = mov_date
        self.genre = mov_genre
