# Python Weather App 🌦️

A beginner-friendly Python application that fetches current weather information for cities around the world using the Open-Meteo API.

## Features

* Search for a city by name.
* Display current temperature in Celsius.
* Show the feels-like temperature.
* Display relative humidity and wind speed.
* Show weather conditions, such as clear skies, rain, and thunderstorms.
* Display the local observation time.
* Handle invalid city names and network errors.
* Search for multiple cities without restarting the program.
* Include automated tests for weather descriptions.

## Technologies Used

* Python
* Requests library
* Open-Meteo Geocoding API
* Open-Meteo Forecast API
* Git and GitHub

## Requirements

* Python 3.10 or newer
* Internet connection

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate into the project folder:

   ```bash
   cd weather-app
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the environment on Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install the dependency:

   ```bash
   python -m pip install requests
   ```

## Usage

Run the application:

```bash
python weather_app.py
```

Enter a city name when prompted. Type `quit` to exit.

## Run Tests

Run the automated tests with:

```bash
python test_weather_app.py
```

## APIs

This project uses the free Open-Meteo APIs:

* Geocoding: https://geocoding-api.open-meteo.com/v1/search
* Weather forecast: https://api.open-meteo.com/v1/forecast

No API key is required for this project.

## Project Structure

```text
weather-app/
├── weather_app.py
├── test_weather_app.py
├── README.md
└── .gitignore
```

## Learning Outcomes

This project demonstrates:

* Python functions and modular programming
* HTTP requests and REST APIs
* JSON data handling
* Input validation and exception handling
* Automated testing
* Virtual environments
* Git and GitHub basics

## Future Improvements

* Add a graphical user interface.
* Display a multi-day forecast.
* Support searching by country and region.
* Build a web version using Flask or Django.

## Author

A Python learning project built to strengthen programming, API integration, and software development skills.
