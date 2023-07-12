# Python
from typing import List

# FastAPI
from fastapi import APIRouter, Path, Query, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# App:
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get(
    path='',
    tags=['movies'],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())]
)
def get_movies() -> List[Movie]:
    """Get all movies"""
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(result))


@movie_router.get(
    path='/{id}',
    tags=['movies'],
    response_model=Movie
    )
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    """Get a movie by ID"""
    db = Session()
    movie = MovieService(db).get_movie(id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Movie not found")
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonable_encoder(movie))

# Para no sobreescribir la url anterior añadimos la / al final


@movie_router.get(
    path='/',
    tags=['movies'],
    response_model=List[Movie]
    )
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movie]:
    """Get a list of movies by category. If there is no movies, returns an
    empty list"""
    db = Session()
    movies = MovieService(db).get_movies_by_category(category)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movies))


@movie_router.post(
    path='/',
    tags=['movies'],
    status_code=status.HTTP_201_CREATED
    )
def create_movie(movie: Movie):
    """Create a new movie in the database"""
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Se ha registrado la película"})


@movie_router.put(
    path='/{id}',
    tags=['movies'],
    response_model=dict
    )
def update_movie(id: int, movie: Movie) -> dict:
    """Update an existent movie by ID"""
    db = Session()
    db_movie = MovieService(db).get_movie(id)
    if not db_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Movie not found")
        
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content={"message": "Se ha modificad la pelicula"})


@movie_router.delete(
    path='/{id}',
    tags=['movies'],
    response_model=dict
    )
def delete_movie(id: int = Path(ge=1, le=2000)) -> dict:
    """Delete an existent movie by ID"""
    db = Session()
    db_movie = MovieService(db).get_movie(id)
    if not db_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Movie not found")
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"message": "Se ha eliminado la película"})
