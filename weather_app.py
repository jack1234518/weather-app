
import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def find_city(city):
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = requests.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, dict):
        return None

    results = data.get("results", [])

    if not isinstance(results, list) or not results:
        return None

    return results[0]


def fetch_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,relative_humidity_2m,"
            "apparent_temperature,wind_speed_10m,weather_code"
        ),
        "timezone": "auto",
    }

    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, dict):
        return None

    current = data.get("current")

    if not isinstance(current, dict):
        return None

    return current


def describe_weather(code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail",
    }

    return descriptions.get(code, "Unknown conditions")


def display_weather(location, current):
    print(f"\nWeather in {location['name']}, {location.get('country', '')}")
    print("-" * 35)
    print(f"Temperature: {current.get('temperature_2m', 'N/A')} °C")
    print(f"Feels like: {current.get('apparent_temperature', 'N/A')} °C")
    print(f"Humidity: {current.get('relative_humidity_2m', 'N/A')}%")
    print(f"Wind speed: {current.get('wind_speed_10m', 'N/A')} km/h")
    print(f"Updated at: {current.get('time', 'N/A')}")
    print(f"Conditions: {describe_weather(current.get('weather_code'))}")


def get_weather(city):
    try:
        location = find_city(city)

        if location is None:
            print("City not found. Please check the spelling and try again.")
            return

        current = fetch_weather(
            location["latitude"],
            location["longitude"],
        )

        if current is None:
            print("Current weather data is unavailable.")
            return

        display_weather(location, current)

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print(f"The weather service returned an error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"An unexpected request error occurred: {error}")

    except (KeyError, ValueError):
        print("The weather service returned invalid data.")



def main():
    print("================================")
    print("       PYTHON WEATHER APP")
    print("================================")

    while True:
        city = input("\nEnter a city (or type 'quit' to exit): ").strip()

        if city.lower() == "quit":
            print("Thanks for using the Weather App!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()