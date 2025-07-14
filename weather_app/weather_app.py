import requests
import sys

def get_weather_data(city_name, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch data ({e})")
        sys.exit()

def display_weather(data, city_name):
    if data.get("cod") != 200:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return

    weather_main = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    print(f"\nWeather in {city_name.capitalize()}:")
    print(f"Condition: {weather_main} ({description})")
    print(f"Temperature: {temp:.1f} °C")
    print(f"Feels like: {feels_like:.1f} °C")
    print(f"Humidity: {humidity}%")

def main():
    api_key = '1a50e26803e5a15bd1bde84dfa83232b'
    city_name = input("Enter your city name: ")

    data = get_weather_data(city_name, api_key)
    display_weather(data, city_name)

if __name__ == "__main__":
    main()
