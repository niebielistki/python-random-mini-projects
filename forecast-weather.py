# forecast-weather.py
# Description: Retrieves and displays a 3-day weather forecast for a specified location using OpenWeatherMap's API.
# Usage: Execute with a city name and country code (ISO 3166-1 alpha-2) as arguments (e.g., forecast-fetcher.py Warsaw PL).

import json
import requests
import sys

# Replace 'YOUR_APPID_HERE' with your actual OpenWeatherMap API key
APPID = 'YOUR_APPID_HERE'

# Ensure correct command line arguments were provided
if len(sys.argv) < 2:
    print('Usage: forecast-fetcher.py city_name, 2-letter_country_code')
    sys.exit()

# Combine command line arguments to form the location query
location = ' '.join(sys.argv[1:])

# Formulate request URL with the user-provided location and API key
url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()  # Check for HTTP request errors

# Convert JSON response into a Python dictionary
weatherData = json.loads(response.text)

# Print the weather forecast
print(f"Current weather in {location}:")
print(weatherData['list'][0]['weather'][0]['main'], '-', weatherData['list'][0]['weather'][0]['description'])
print('\nTomorrow:')
print(weatherData['list'][1]['weather'][0]['main'], '-', weatherData['list'][1]['weather'][0]['description'])
print('\nDay after tomorrow:')
print(weatherData['list'][2]['weather'][0]['main'], '-', weatherData['list'][2]['weather'][0]['description'])
