import requests

country = input("For which country do you want the weather forecast? ")
city = input("For which city do you want the weather forecast? ")

url = f"https://api.weatherapi.com/v1/current.json?key=336ec2477a07417f8c5141903250812&q={city}, {country}&aqi=no"
response = requests.get(url)

weather = response.json()

print(f"Local time in {city}, {country}: {weather['location']['localtime']}")
print(f"It's currently {weather['current']['temp_c']}°C, feels like {weather['current']['feelslike_c']}°C.")