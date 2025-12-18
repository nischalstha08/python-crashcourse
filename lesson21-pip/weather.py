import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather():
    print('\n** Get Curent Weather Conditions **\n')
    
    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    print(request_url)
    
get_current_weather()