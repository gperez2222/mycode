#!/usr/bin/env python3

""" Use an open API example to return the weather """

# import required modules

import requests, json

# Enter your API key here
#api_key = "Your_API_Key"
api_key = "6c8908cb4b9e383b4af05947cde8d465"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = print("Enter City Name: ", input("Enter city name : "))

# create the complete_url variable 
complete_url = f"{base_url}appid={api_key}&q={city_name}"

print(complete_url)

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found

#if x["cod"] != "404":
#
#	# store the value of "main"
#	# key in variable y
#	y = x["main"]
#
#	# store the value corresponding
#	# to the "temp" key of y
#	current_temperature = y["temp"]
#
#	# store the value corresponding
#	# to the "pressure" key of y
#	current_pressure = y["pressure"]
#
#	# store the value corresponding
#	# to the "humidity" key of y
#	current_humidity = y["humidity"]
#
#	# store the value of "weather"
#	# key in variable z
#	z = x["weather"]
#
#	# store the value corresponding
#	# to the "description" key at
#	# the 0th index of z
#	weather_description = z[0]["description"]
#
#	# print following values
#	print(" Temperature (in kelvin unit) = " +
#					str(current_temperature) +
#		"\n atmospheric pressure (in hPa unit) = " +
#					str(current_pressure) +
#		"\n humidity (in percentage) = " +
#					str(current_humidity) +
#		"\n description = " +
#					str(weather_description))
#
#else:
#	print(" City Not Found ")
###
