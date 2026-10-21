import re
from api_client import get_json

GEO_API_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORCAST_API_URL = "https://api.open-meteo.com/v1/forecast"


def find_city(GEO_API_URL, city):
    geo_details = get_json(GEO_API_URL, params=(
        {"name": city, "count": 1}), timeout=10)

    if not geo_details or not geo_details.get("results", None):
        raise ValueError(f"No geo details found for city : {city}")

    print(geo_details)
    return geo_details["results"][0]["latitude"], geo_details[
        "results"][0]["longitude"], geo_details["results"][0]["country"]


def get_weather_forecast(FORCAST_API_URL, latitude, longitude):

    forecast = get_json(FORCAST_API_URL, params=(
        {"latitude": latitude, "longitude": longitude, "current": ["temperature_2m", "wind_speed_10m"]}), timeout=10)

    if not forecast:
        raise ValueError("Forecast not found")

    print(forecast)
    # return forecast["current"]["temperature_2m"], forecast["current"]["wind_speed_10m"] | forecast["current"]["temperature_2m"], forecast["current_units"]["wind_speed_10m"]
    return forecast


def know_weather():
    while (True):
        try:
            city = input(
                "Enter city or '/q' to quit: ").strip().lower()

            if city == '/q':
                break

            if not city:
                raise ValueError("City should not be empty")
            if not re.match(r"^[a-zA-Z\s\-]+$", city):
                raise ValueError("City should be a String")

            latitude, longitude, country = find_city(GEO_API_URL, city)
            print(f"{latitude:<10} l{longitude:<10}")

            forecast = get_weather_forecast(
                FORCAST_API_URL, latitude, longitude)

            print('*' * 50)
            print(f"{"Weather Report":^50}")
            print('*' * 50)
            print(
                f"{city}, {country} {forecast["current"]["temperature_2m"]} {forecast["current_units"]["temperature_2m"]}"
                f" wind {forecast["current"]["wind_speed_10m"]} {forecast["current_units"]["wind_speed_10m"]} ")

        except ValueError as error:
            print(error)


def main():
    know_weather()


main()
