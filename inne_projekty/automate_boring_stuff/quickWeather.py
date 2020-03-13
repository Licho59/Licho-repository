#! python3
# quickWeather.py - Prints the weather for the location from the command line.
# !!! http://api.openweathermap.org/ requires registering to get key
import json, requests, sys

# computing location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# downloading JSON data from OpenWeatherMap.org's API
url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q-{location}&cnt=3'
response = requests
.get(url)
response.raise_for_status()

# loading JSON data into Python variable
weatherData = json.loads(response.text)

# printing weather descriptions
w = weatherData['list']
print(f'Current weather in {location}')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], ',', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

      
