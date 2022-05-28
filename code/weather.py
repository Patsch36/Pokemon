import requests
import json
import geocoder

# login data sbas..gmail.com, python_IN20

class Weather:
    def __init__(self):
        location = geocoder.ip("me").city
        self.url_weather = "https://api.weatherapi.com/v1/current.json?key="
        self.url_key = "9f55021b1fcc4122892123728220905 &q=" + location + "&aqi=no"
        self.url = str(self.url_weather + self.url_key)
        location = geocoder.ip("me").city
        # log print(self.url)
        
    def __weather_mapped(self, row_weather_data):
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
    
