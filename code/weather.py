
import requests
import json
import geocoder



class Weather:
    """Class Weater gets wetter condition of your location (over ip tracker)
    """
    def __init__(self):
        """prepare url for API request and get location
        """
        try:
            location = geocoder.ip("me").city
        except TypeError as err:
            print(err)
            location = "Stuttgart" # log Stuttgart as deafault cause of no connection
        self.url_weather = "https://api.weatherapi.com/v1/current.json?key="    # login data sbas..gmail.com, python_IN20
        self.url_key = "9f55021b1fcc4122892123728220905 &q=" + location + "&aqi=no" # key hidding was skipped cause of time
        self.url = str(self.url_weather + self.url_key)

        # log print(self.url)
        
    def __weather_mapped(self, row_weather_data):
        """_summary_

        :param row_weather_data: _description_
        :type row_weather_data: _type_
        :return: _description_
        :rtype: _type_
        """
        data = {'Partly cloudy': 'cloud', 'Rainy': 'rain', 'Sunny':'sun', 'Snowing': 'snow'}
        return data[row_weather_data]
        
    def get_weather_text(self):
        try:
            file_data  = requests.get(self.url)
        except requests.ConnectionError as err:
            print(err)
            # log connection error weather api
        data = file_data.json()
        weather = data['current']['condition']
        weather = str(weather['text'])
        #map all conditions to cloudy, rain, sun, snow (jahreszeit?)
        weather = self.__weather_mapped(weather)
        return weather
    
    def get_weather_code(self):
        try:
            file_data  = requests.get(self.url)
        except requests.ConnectionError as err:
            print(err)
            # log connection error weather api
        data = file_data.json()
        weather = data['current']['condition']
        # log weather: weather # (code)
        return weather['code']
    
