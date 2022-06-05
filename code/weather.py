"""
:author: Sascha Bäuerle
:name: language.py
:created: 16. Mai 2022
:description: Contains class Weather 
"""
import sys
import requests
import json
import geocoder
from datetime import date
import logging



class Weather:
    """Class Weater gets wetter condition of your location (over ip tracker)

    Attributes:
        url_weather: String   :   Url of the API
        url_key: String   :   API Auth token and location
        url: String   :   Concatenated String of url_weather + url_key
    """
    def __init__(self):
        try:
            geocoder_ip = geocoder.ip("me")
            location = str(geocoder_ip.city)
            self.coords = geocoder_ip.latlng
            logging.debug("Location: " + str(location))
        except TypeError as err:
            print(err)
            location = "Stuttgart" # log Stuttgart as deafault cause of no connection
            sys.exit()
        self.url_weather = "https://api.weatherapi.com/v1/current.json?key="    # login data sbas..gmail.com, python_IN20
        self.url_key = "9f55021b1fcc4122892123728220905&q=" + location + "&aqi=no" # key hidding was skipped cause of time
        self.url = str(self.url_weather + self.url_key)
        self.weather_text = False

        # log print(self.url)
        
    def __weather_mapped(self, row_weather_data):
        """Mapps the entrance string to workable strings

        :param row_weather_data: Data from the weather api
        :type row_weather_data: String
        :return: the mapped string 
        :rtype: String
        """
        data = {'Partly cloudy': 'cloud', 'Rainy': 'rain', 'Sunny':'sun', 'Snowing': 'snow'}
        return data[row_weather_data]

    def getSnow(self):
        """Query if it snowing

        :return: True if it snowing, False if no
        :rtype: Bool
        """
        if not self.weather_text:
            self.weather_text = self.get_weather_text()
        month = date.today().month
        if(self.coords[0] > 0) and (month in [1, 11, 12]) and ( self.weather_text != 'rain'):
            return True
        elif (self.coords[0] < 0) and (month in [6, 7, 8]) and ( self.weather_text != 'rain'):
            return True
        return False
        
    def get_weather_text(self):
        """Query for the actuall weather text(unmapped)

        :return: Weather condition as text
        :rtype: String
        """
        try:
            file_data  = requests.get(self.url)
        except requests.ConnectionError as err:
            print(err)
            # log connection error weather api
        data = file_data.json()
        weather = data['current']['condition']
        weather = str(weather['text'])
        #map all conditions to cloudy, rain, sun, snow (jahreszeit?)
        weather = "rain"#self.__weather_mapped(weather)
        return weather
    
    def get_weather_code(self):
        """Query for the actuall weather code

        :return: Weather code
        :rtype: int
        """
        try:
            file_data  = requests.get(self.url)
        except requests.ConnectionError as err:
            print(err)
            # log connection error weather api
        data = file_data.json()
        weather = data['current']['condition']
        # log weather: weather # (code)
        return weather['code']
    
