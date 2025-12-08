import requests

api_key = "YOUR_API_KEY_HERE"

country = input("For which country do you want the weather forecast? ")
city = input("For which city do you want the weather forecast? ")

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}, {country}&aqi=no"
response = requests.get(url)

if not response.ok:
    print("Error fetching the weather data.")
    exit()

weather_json = response.json()

local_time = weather_json['location']['localtime']
weather = weather_json['current']['temp_c']
feels_like = weather_json['current']['feelslike_c']

print(f"Local time in {city}, {country}: {local_time}")
print(f"It's currently {weather}°C, feels like {feels_like}°C.")