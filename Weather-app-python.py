# Weather App using Python and OpenWeather API

import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter City Name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if str(data["cod"]) == "200":
    print("\n========== WEATHER INFORMATION ==========\n")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Humidity: {data['main']['humidity']} %")
    print(f"Weather: {data['weather'][0]['main']}")
    print(f"Description: {data['weather'][0]['description']}")
else:
    print(f"Error: {data['message']}")
