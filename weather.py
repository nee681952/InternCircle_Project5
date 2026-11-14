import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_KEY")

# OpenWeather API URL
URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

print("Weather App")
print("API key loaded:", bool(API_KEY))

def get_weather(city):

    if not API_KEY:
        print("API key not found. Check your .env file.")
        return None

    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            URL,
            params=params,
            timeout=10
        )

        if response.status_code == 404:
            print("City not found. Please check the city name.")
            return None

        if response.status_code == 401:
            print("Invalid or inactive API key.")
            return None

        if response.status_code != 200:
            print("API error:", response.status_code)
            return None

        return response.json()

    except requests.exceptions.RequestException:
        print("Network problem. Please check your internet connection.")
        return None

def display_weather(data):
    city_name = data.get("name", "Unknown")

    main_data = data.get("main", {})
    weather_list = data.get("weather", [])
    wind_data = data.get("wind", {})

    temperature = main_data.get("temp", "N/A")
    humidity = main_data.get("humidity", "N/A")
    wind_speed = wind_data.get("speed", "N/A")

    if weather_list:
        description = weather_list[0].get("description", "N/A")
    else:
        description = "N/A"

    print("\n------ Weather Report ------")
    print("City:", city_name)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", description)
    print("Wind Speed:", wind_speed, "m/s")
    print("----------------------------")

def get_forecast(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            FORECAST_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 404:
            print("City not found.")
            return None

        if response.status_code == 401:
            print("Invalid or inactive API key.")
            return None

        if response.status_code != 200:
            print("Forecast API error:", response.status_code)
            return None

        return response.json()

    except requests.exceptions.RequestException:
        print("Network problem while fetching forecast.")
        return None

def display_forecast(data):
    forecast_list = data.get("list", [])

    print("\n------ 5-Day Forecast ------")
    print(f"{'Date & Time':<22} {'Temp':<10} {'Description'}")
    print("-" * 55)

    shown_dates = set()

    for item in forecast_list:
        date_time = item.get("dt_txt", "")
        date = date_time.split(" ")[0]

        if date and date not in shown_dates:
            main_data = item.get("main", {})
            weather_list = item.get("weather", [])

            temperature = main_data.get("temp", "N/A")

            if weather_list:
                description = weather_list[0].get(
                    "description", "N/A"
                )
            else:
                description = "N/A"

            print(f"{date_time:<22} {temperature:<10} {description}")

            shown_dates.add(date)

        if len(shown_dates) == 5:
            break

print("\n================================")
print("       WEATHER APPLICATION")
print("================================")

while True:
    city = input("\nEnter city name (or press Enter to exit): ").strip()

    if city == "":
        print("Thank you for using Weather App!")
        break

    weather_data = get_weather(city)

    if weather_data:
        display_weather(weather_data)

        forecast_data = get_forecast(city)

        if forecast_data:
            display_forecast(forecast_data)