# Example 6: Movie Class
# A class representing a movie with attributes for title, director, and release year, and methods to get movie details and check if the movie is old (more than 20 years).

class Movie:
    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    
    def get_movie(self):
        return f"{self.title} directed by {self.director}, released in {self.release_year}"
    
    def is_old(self):
        current_year = 2024
        if (current_year - self.release_year) > 20:
            print(f"{self.title} is old movie")
        else:
            print(f"{self.title} is new movie")
    

#usage
movie1 = Movie("bhool bhoolaiya", "priyadarshan", 2008)
print(movie1.get_movie())
movie1.is_old()