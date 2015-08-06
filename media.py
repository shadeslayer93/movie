import webbrowser

class Movie():
    """This is the Movie template based on which other 
       instances are created !! """
       
    def __init__(self, movie, trailer, poster, story):
    	self.title = movie
		self.trailer_youtube_url = trailer
		self.poster_image_url = poster
		self.story_line = story

    def show_trailer(self):
    	webbrowser.open(self.trailer_youtube_url)