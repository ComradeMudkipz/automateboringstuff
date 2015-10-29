#! /usr/bin/python3
# quickWeather.py - Prints the weather for a location from the command line.
# TODO: Use a proper API key (paid)


import json
import requests
import sys


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = """http://api.openweathermap.org/data/2.5/forcast/daily?q=%s&mode=json&appid
         =eedbb989958042d3a84a651529ac4e19""" % (location)      # change appid to paid
                                                                # api key for functionality
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
