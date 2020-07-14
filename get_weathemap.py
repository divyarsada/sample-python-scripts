import requests
from argparse import ArgumentParser
import sys
import os, json
#Get the Cityname from the commandline
parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('city_name',help='Provide the name of the city for which weather info is needed')
args = parser.parse_args()
#Get the api env variable
api_key= os.getenv('OWM_API_KEY')
#url = f"http://api.openweathermap.org/data/2.5/weather?id={args.city}&appid={api_key}"
url=f"http://api.openweathermap.org/data/2.5/weather?q={args.city_name}&appid={api_key}"
#Check if api key is available
if not api_key:
    print("Error: no api key provided")
    sys.exit(1)
#Download the JSON data from OpenWeatherMap.org's API
response = requests.get(url)
#Validate if the response status is success
if response.status_code !=200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

#Load JSON data into a Python variable
weather_info_dict = json.loads(response.text)
print(f'Current weather in {args.city_name}:')
print(weather_info_dict['weather'][0]['main'],'-', weather_info_dict['weather'][0]['description'])

