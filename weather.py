#!/usr/bin/env python3

# import required modules

import requests, json

from pprint import pprint

# Enter your API key here
#api_key = "Your_API_Key"
api_key = "6c8908cb4b9e383b4af05947cde8d465"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

default_city_name = "Cliffside Park"

# Give city name
city_name = input("Enter City Name or \"q\" for quit, for ex: [ Cliffside Park (def)]:  ")

if "q" in city_name:
    print(f"Exiting")
    exit()

if len(city_name) == 0:
    city_name = default_city_name

# compose the complete_url variable 
#complete_url = base_url + "appid=" + api_key + "&q=" + city_name
complete_url = f"{base_url}appid={api_key}&q={city_name}&units=imperial"

#print(f"\nSearching weather for \"{city_name}\" using URL:{complete_url}\n")

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
json_output = response.json()

##pprint(json_output)

# Now json_output contains list of nested dictionaries, check the value of "cod" key is equal to "404", 
# means city is found otherwise city is not found

if json_output["cod"] != "404":

	# store the value of "main" key in variable mainpage
    mainpage = json_output["main"]

	# store the value corresponding
	# to the "temp" key of mainpage
    current_temperature = mainpage["temp"]

	# store the value corresponding
	# to the "pressure" key of mainpage
    current_pressure = mainpage["pressure"]

	# store the value corresponding
	# to the "humidity" key of mainpage
    current_humidity = mainpage["humidity"]

	# store the value of the "weather" key in variable "weather"
    weather = json_output["weather"]

	# store the value corresponding to the "description" key at the 0th index of weather
    weather_description = weather[0]["description"]

    # print following values
    print(f"{city_name}: {weather_description}, Temp: {current_temperature} Far: Hum: {current_humidity}%")

else:
    print(f" {city_name} Not Found ")

