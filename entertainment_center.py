import fresh_tomatoes
import media

# Data file instantiating new Movie objects (defined in media.py) that then adds them to a movies list.
# A new webpage is created from this list (defined in fresh_tomatoes.py) and shown in the web browser.

fantastic_mr_fox = media.Movie("Fantastic Mr. Fox", "https://dg7kra6zb39sn.cloudfront.net/media/spotlight/page/poster-0f39d152-d30c-455f-a94e-ee9596b9cc5b.jpg", "https://www.youtube.com/watch?v=n2igjYFojUo")
grand_budapest = media.Movie("The Grand Budapest Hotel", "https://images-na.ssl-images-amazon.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=1Fg5iWmQjwk")
hot_fuzz = media.Movie("Hot Fuzz", "http://t2.gstatic.com/images?q=tbn:ANd9GcSlM2Ugu41GcdkqjVA7SLQeOZD6nWibTotxJPkTasDC8GkMypRL", "https://www.youtube.com/watch?v=ayTnvVpj9t4")
martian = media.Movie("The Martian", "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ", "https://www.youtube.com/watch?v=ej3ioOneTy8")
bourne_id = media.Movie("The Bourne Identity", "http://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v8_ai.jpg", "https://www.youtube.com/watch?v=cD-uQreIwEk")
i_robot = media.Movie("I, Robot", "http://www.gstatic.com/tv/thumb/movieposters/34586/p34586_p_v8_ap.jpg", "https://www.youtube.com/watch?v=rL6RRIOZyCM")

# Put Movie object references into movies array
movies = [fantastic_mr_fox, grand_budapest, hot_fuzz, martian, bourne_id, i_robot]

# Use the list of references to create a new webpage displaying the movies we've chosen
fresh_tomatoes.open_movies_page(movies)