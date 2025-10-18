from lib.API_handler import API_handler
from datetime import datetime

# parse for openweather specific JSON 
# move it form API_handler.py parse-function

class Openweather(API_handler):

    def __init__(self, url:str):
        super().__init__()
        self.parsed_data = {}
        self.url = url
        self.keys = ["now", "+3h", "+6", "+9"]


    def parse_data(self):
        # get data 
        self.data = self.get_posts(self.url)
            
        # parsing data
        self.parsed_data['city'] = self.data['city']
        for idx, key in enumerate(self.keys):
            self.parsed_data[key] = self.data["list"][idx]

        # retrn data
        if self.parsed_data is None:
            return None
        else:
            return self.parsed_data


    def __str__(self):
        if self.parsed_data == {}:
            if self.data == None:
                return "No data availible yet"
            
            else: 
                return self.data
        
        else:
            return self.print_parsed_data()
        

    def print_parsed_data(self) -> str:
        if self.parsed_data == {}:
            return "No parsed data availible yet"

        else:
            city:dict = self.parsed_data["city"]
            string = ""
            string +=f"City: {city["name"]}\n"
            
            string += f"Sunrise: {self.str_from_timestamp(city["sunrise"])}\n"

            string += f"Sunrise: {self.str_from_timestamp(city["sunset"])}\n"

            for key in self.keys:
                string += f"\n{key}\n"

                main = self.parsed_data[key]["main"]
                weather = self.parsed_data[key]["weather"][0]
                wind = self.parsed_data[key]["wind"]

                string += f"Temperature: {main["temp"]}°C\n"
                string += f"Feels like: {main["feels_like"]}\n"

                string += f"Description: {weather["main"]}\n"

                string += f"Wind speed: {wind["speed"]}m/s\n"
                string += f"Wind direction: {self.degree_to_direction(float(wind["deg"]), long_string= True)}\n"

                string += "\n"

            return string


    @staticmethod
    def str_from_timestamp(ts:str) -> str:
        return datetime.fromtimestamp(int(ts)).strftime('%H:%M:%S')
    

    @staticmethod
    def degree_to_direction(degree:float, long_string:bool = False, de_en:bool = False) -> str:
        wind_direction_long_de = {
            "N": "Norden",
            "NO": "Nordosten",
            "O": "Osten",
            "SO": "Südosten",
            "S": "Süden",
            "SW": "Südwesten",
            "W": "Westen",
            "NW": "Nordwesten"
        }
        
        wind_direction_long_en = {
            "N": "North",
            "NO": "Northeast",
            "O": "East",
            "SO": "Southeast",
            "S": "South",
            "SW": "Southwest",
            "W": "West",
            "NW": "Northwest"
        }
        
        if (degree >= 337.5 or degree < 22.5): 
            direction = "N"  
        elif (degree >= 22.5 and degree < 67.5):
            direction = "NO"
        elif (degree >= 67.5 and degree < 112.5):
            direction = "O"
        elif (degree >= 112.5 and degree < 157.5):
            direction = "SO"
        elif (degree >= 157.5 and degree < 202.5):
            direction = "S"
        elif (degree >= 202.5 and degree < 247.5):
            direction = "SW"
        elif (degree >= 247.5 and degree < 292.5):
            direction = "W"
        elif (degree >= 292.5 and degree < 337.5):
            direction = "NW"
        else:
            direction = "N/A"
            return direction
        
        if long_string:
            if de_en:
                direction = wind_direction_long_de[direction]
            else:
                direction = wind_direction_long_en[direction]
        
        return direction
