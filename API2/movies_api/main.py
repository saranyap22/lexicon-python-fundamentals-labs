from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
movies = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan", "year": 2010},
    {"id": 2, "title": "Avatar", "director": "James Cameron", "year": 2009},
    {"id": 3, "title": "The God Father",
        "director": "Fransis Ford Copola", "year": 2010},
    {"id": 4, "title": "Titanic", "director": "James Cameron", "year": 1997}
]


class Movie(BaseModel):
    title: str
    director: str
    year: int


@app.get("/movies")
def get_movies(director: str | None, year: int | None):
    result = movies

    if director is not None:
        result = [mov for mov in movies if mov["director"] == director]
    if year is not None:
        result = [mov for mov in result if mov["year"] == year]

    return result


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    existing = find_movie(movie_id)
    if existing is not None:
        return existing

    raise HTTPException(status_code=404, detail="Movie not found")


@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    movie_id = max((movie["id"] for mov in movies), default=0) + 1
    new_movie = {"id": movie_id, "title": movie.title,
                 "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie


@app.put("/movies/{movie_id}", status_code=200)
def update_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    if existing is not None:
        existing["title"] = movie.title
        existing["director"] = movie.director
        existing["year"] = movie.year
        return existing

    raise HTTPException(status_code=404, detail="Movie not found")


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    if existing is not None:
        movies.remove(existing)


def find_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
