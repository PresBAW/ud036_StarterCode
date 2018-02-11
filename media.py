# Main class for instantiating Movie objects
class Movie():
	# Initialize new Movie objects with title, poster art, and youtube trailer link
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
