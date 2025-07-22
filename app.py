import requests
api_key="6555c3e2e244bd3e3c849b3434312e92"
def weather_report(api_key):
    user_input=input("Enter the city: ")
    print(user_input)
    weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")
    weatherreport=weather_data.json()
    data=weather_data.status_code
    if (data==200):
        weather = weatherreport["weather"][0]["description"].title()
        temperature = weatherreport["main"]["temp"]
        humidity = weatherreport["main"]["humidity"]
        wind_speed = weatherreport["wind"]["speed"]
        city_name = weatherreport["name"]
        country = weatherreport["sys"]["country"]

        print(f"\nWeather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    elif(data==404):
        print("City not found. Please try again.")
weather_report(api_key)