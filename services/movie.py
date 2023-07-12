from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_movies(self):
        movies = self.db.query(MovieModel).all()
        return movies
    
    def get_movie(self, id):
        movies = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return movies
    
    def get_movies_by_category(self, category):
        movies = self.db.query(MovieModel).filter(
            MovieModel.category == category).all()
        return movies
    
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return 
    
    def update_movie(self, id: int, movie: Movie):
        db_movie = self.get_movie(id)
        db_movie.title = movie.title
        db_movie.overview = movie.overview
        db_movie.year = movie.year
        db_movie.category = movie.category
        db_movie.rating = movie.rating
        self.db.commit()
        return
    
    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return 
        
        