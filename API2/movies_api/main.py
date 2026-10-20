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


class UpdateMovie(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
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
    movie_id = max((mov["id"] for mov in movies), default=0) + 1
    new_movie = {"id": movie_id, "title": movie.title,
                 "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie


@app.put("/movies/{movie_id}", status_code=200)
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    if existing is not None:
        existing["title"] = movie.title
        existing["director"] = movie.director
        existing["year"] = movie.year
        return existing

    raise HTTPException(status_code=404, detail="Movie not found")


@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, changes: UpdateMovie):
    existing = find_movie(movie_id)
    if existing is not None:
        existing.update(changes.model_dump(exclude_unset=True))
        return existing

    raise HTTPException(status_code=404, detail="Movie not found")

# -----------------------Testing edge cases - comments for update_movie-------------
# 1. update some fields - status 200, specific fields updated
# 2. year as number in text("1990") in update- status 200, year converted to int and updated
# 3. year as text in update- status- 422 (Unprocessable content)
# 4. invalid id in path("abc")- status - 422 (Unprocessable content)
# 5. id not exist - status - 404 (Movie not found)
# ---------------------------------------------------------------------

# PUT: Replaces existing data with new data client sent. preferred when data is small and want idempotent feature for update automatically
# PATCH: Update only few requested fields. Requires that fields are optinoal. Suitable for larger payloads where repeating data is wasteful

# -----------------------------------------------------------------------


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    if existing is not None:
        movies.remove(existing)


def find_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
