# from flask import Flask, render_template, request
# from weather import get_current_weather
# from waitress import serve

# app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/weather')
# def get_weather():
#     city = request.args.get('city')
#     weather_data = get_current_weather(city)
#     return render_template(
#         "weather.html",
#         title=weather_data["name"],
#         status=weather_data["weather"][0]["description"].capitalize(),
#         temp=f"{weather_data['main']['temp']:.1f}",
#         feels_like=f"{weather_data['main']['feels_like']:.1f}"
#     )


# if __name__ == "__main__":
#     serve(app, host="0.0.0.0", port=8000)



from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    # Get city from query parameters and strip whitespace
    city = request.args.get('city', '').strip()
    
    # Validate that city was provided
    if not city:
        return render_template('index.html', error="Please enter a city name")
    
    # Get weather data
    weather_data = get_current_weather(city)
    
    # Check if there was an error getting weather data
    if "error" in weather_data:
        return render_template('index.html', error=weather_data["error"])
    
    # Validate response structure and render weather page
    try:
        return render_template(
            "weather.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}",
            humidity=weather_data['main'].get('humidity', 'N/A'),
            wind_speed=f"{weather_data['wind'].get('speed', 0):.1f}"
        )
    except (KeyError, IndexError, TypeError) as e:
        # Log the error for debugging
        print(f"Error parsing weather data: {e}")
        print(f"Weather data received: {weather_data}")
        return render_template(
            'index.html', 
            error="Unable to parse weather data. Please try again."
        )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('index.html', error="Internal server error occurred"), 500

if __name__ == "__main__":
    # Check if API key is configured
    if not os.getenv("API_KEY"):
        print("WARNING: API_KEY not found in environment variables!")
        print("Please create a .env file with your OpenWeatherMap API key")
    
    print("Starting Weather App Server...")
    print("Access the app at: http://localhost:8000")
    serve(app, host="0.0.0.0", port=8000)