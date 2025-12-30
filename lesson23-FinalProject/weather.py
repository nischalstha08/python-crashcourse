# from dotenv import load_dotenv
# from pprint import pprint
# import requests
# import os

# load_dotenv()

# def get_current_weather(city="Kathmandu"):
#     request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
#     weather_data = requests.get(request_url).json()
    
#     return weather_data

# if __name__ == "__main__":
#     print('\n*** Get Current Weather Status ***\n')
    
#     city = input("\nPlease enter a city name:")
    
#     weather_data = get_current_weather(city)
    
#     print("\n")
#     pprint(weather_data)


from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Load environment variables from .env file
load_dotenv()

def get_current_weather(city="Kathmandu"):
    """
    Fetch current weather data for a given city using OpenWeatherMap API.
    
    Args:
        city (str): Name of the city to get weather for
        
    Returns:
        dict: Weather data or error dictionary
    """
    
    # Validate input
    if not city or not city.strip():
        return {"error": "City name cannot be empty"}
    
    # Clean the city name
    city = city.strip()
    
    # Check if API key exists
    api_key = os.getenv("API_KEY")
    if not api_key:
        return {"error": "API key not configured. Please add API_KEY to your .env file"}
    
    # Construct the API request URL
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric'
    
    try:
        # Make the API request with timeout
        response = requests.get(request_url, timeout=10)
        
        # Check for HTTP errors
        if response.status_code == 200:
            weather_data = response.json()
            
            # Validate that we got expected data structure
            if "main" in weather_data and "weather" in weather_data:
                return weather_data
            else:
                return {"error": "Unexpected API response format"}
                
        elif response.status_code == 404:
            return {"error": f"City '{city}' not found. Please check the spelling and try again"}
        
        elif response.status_code == 401:
            return {"error": "Invalid API key. Please check your API_KEY in .env file"}
        
        elif response.status_code == 429:
            return {"error": "API rate limit exceeded. Please try again later"}
        
        else:
            return {"error": f"API error: Unable to fetch weather data (Status: {response.status_code})"}
    
    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please check your internet connection and try again"}
    
    except requests.exceptions.ConnectionError:
        return {"error": "Network connection error. Please check your internet connection"}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: Unable to connect to weather service"}
    
    except ValueError:
        return {"error": "Invalid response from weather API"}
    
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error in get_current_weather: {e}")
        return {"error": "An unexpected error occurred while fetching weather data"}


if __name__ == "__main__":
    """
    Run this script directly to test weather fetching from command line
    """
    print('\n*** Get Current Weather Status ***\n')
    
    # Check if API key is configured
    if not os.getenv("API_KEY"):
        print("ERROR: API_KEY not found!")
        print("Please create a .env file with your OpenWeatherMap API key")
        print("Example: API_KEY=your_api_key_here")
        exit(1)
    
    # Get city input from user
    city = input("\nPlease enter a city name (or press Enter for Kathmandu): ").strip()
    
    # Use default if no city provided
    if not city:
        city = "Kathmandu"
        print(f"Using default city: {city}")
    
    # Fetch weather data
    print(f"\nFetching weather data for {city}...\n")
    weather_data = get_current_weather(city)
    
    # Display results
    if "error" in weather_data:
        print(f"ERROR: {weather_data['error']}")
    else:
        print("Weather Data:")
        print("-" * 50)
        pprint(weather_data)
        print("-" * 50)
        print(f"\nCity: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']:.1f}°C")
        print(f"Feels Like: {weather_data['main']['feels_like']:.1f}°C")
        print(f"Condition: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")