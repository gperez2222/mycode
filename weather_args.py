#!/usr/bin/env python3

# import required modules

import sys
import getopt

import requests, json

from pprint import pprint

# Enter your API key here
#api_key = "Your_API_Key"
api_key = "6c8908cb4b9e383b4af05947cde8d465"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

default_city_name = "Cliffside Park"

########################################################

def cityArgs(argv):

    city_name = ""

    arg_help = "{0} -h -c <city name>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hc:", ["help", "city="])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-c", "--city"):
            city_name = arg

    if len(city_name) == 0:
        # if there were no arguemts passwd for the city name then prompt for input
        city_name = input("Enter City Name or \"q\" for quit, for ex: [ Cliffside Park (def)]:  ")

        if "q" in city_name:
            print(f"Exiting")
            exit()
    
        if len(city_name) == 0:
            city_name = default_city_name

    return(city_name)

########################################################

def main():

    city_name = cityArgs(sys.argv)

    # compose the complete_url variable 
    #complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=imperial"
    
    # get method of requests module and return response object
    response = requests.get(complete_url)
    
    # json method of response object and convert json format data into python format data
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
        #current_pressure = mainpage["pressure"]

	    # store the value corresponding
	    # to the "humidity" key of mainpage
        current_humidity = mainpage["humidity"]
    
	    # store the value of the "weather" key in variable "weather"
        weather = json_output["weather"]
    
	    # store the value corresponding to the "description" key at the 0th index of weather
        weather_description = weather[0]["description"]

        # print following values
        print(f"{city_name} - {weather_description} - Temp: {current_temperature} Far - Hum: {current_humidity}%")

    else:
        print(f" {city_name} Not Found ")

if __name__ == "__main__":
    main()

