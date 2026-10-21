import requests
import os
from api_client import get_json
from dotenv import load_dotenv

BASE_URL = "http://127.0.0.1:8000"


def load_api_key():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    if not API_KEY or not API_KEY.strip():
        raise RuntimeError("Api key is not configured or empty")


def get_movies():
    movies = get_json(f"{BASE_URL}/movies", timeout=5)

    if movies:
        for movie in movies:
            print(
                f"{movie["title"]:<20} {movie["director"]:<20} {movie["year"]:^6}")


def create_movie(headers=None):
    new_movie = {
        "title": "Amman", "director": "Kodi Ramakrishna", "year": 1995
    }
    try:

        response = requests.post(
            f"{BASE_URL}/movies", json=new_movie, headers=headers, timeout=5)
        response.raise_for_status()

        movie = response.json()
        if movie:
            print(movie["id"], movie["title"],
                  movie["director"], movie["year"])
    except requests.exceptions.HTTPError as error:
        print(
            f"The server did not serve the request: reason {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The response was not a JSON")
    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {type(error).__name__}")


def main():
    load_api_key()
    headers = {"X-API-Key": os.getenv("API_KEY")}
    create_movie(headers)
    create_movie()


main()
