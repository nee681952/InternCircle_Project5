# Weather App with Live OpenWeather API

## Project Overview
A Python-based weather application that fetches real-time weather information and a 5-day forecast for a city using the OpenWeather API.

## Features
- Search weather by city name
- Display temperature in Celsius
- Display humidity and weather description
- Display wind speed
- Show a 5-day forecast
- Handle invalid city names and API errors
- Protect the API key using environment variables

## Technologies Used
- Python
- Requests
- python-dotenv
- OpenWeather API

## Installation

1. Install Python.
2. Install the required packages:

```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project folder:

```text
OPENWEATHER_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key. Never publish this file.

## Run the Application

```bash
python weather.py
```

Enter a city name to view its current weather and forecast. Press Enter without entering a city to exit.

## API Key Security

The API key is stored in a local `.env` file and loaded using `python-dotenv`. The `.env` file is included in `.gitignore` so it is not uploaded to GitHub.

## Author
Neeraj J