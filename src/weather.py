import requests

class WeatherData:
    def __init__(self, longitude: str, latitude: str):
        self.url = f"https://api.open-meteo.com/v1/forecast" 
        self.longitude = longitude
        self.latitude = latitude

    def celsius_to_fahrenheit(self, celsius):
        """Convert Temperature from Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32
    
    def weather_code_to_description(self, weather_code):
        """Convert Open-Meteo weather code to a human-readable description."""
        mapping = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            56: "Light freezing drizzle",
            57: "Dense freezing drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            66: "Light freezing rain",
            67: "Heavy freezing rain",
            71: "Slight snow fall",
            73: "Moderate snow fall",
            75: "Heavy snow fall",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail",
        }
        return mapping.get(weather_code, "Unknown weather code")

    def get_current_weather(self):
        return requests.get(f"{self.url}?latitude={self.latitude}&longitude={self.longitude}&current_weather=true").json()
    
    def print_current_weather(self):
        weather = self.get_current_weather().get("current_weather", {})

        if weather:
            temp = self.celsius_to_fahrenheit(weather.get("temperature"))
            windspeed = weather.get("windspeed")
            description = self.weather_code_to_description(weather.get("weathercode"))
            
            print(f"Temperature: {temp}°F")
            print(f"Windspeed: {windspeed}")
            print(f"Description: {description}")
        else:
            print("No weather available. Check your API endpoint to see if it still works")
