import requests

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Fetching data from OpenWeatherMap API
    response = requests.get(complete_url)
    data = response.json()
    
    # Checking if the city is found
    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Extracting weather information
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_desc = weather_data["description"]
        
        # Printing weather details
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_desc.capitalize()}\n")
    else:
        print("City not found!")

# Main function
def main():
    print("Simple Weather Program\n")
    city = input("Enter city name: ")
    api_key = "90b7bdf7b2971f8002f9335335901802"  
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
