from lib.Config import config
from Openweather import Openweather
import lib.logger

def main():  
    path = config.get_path_prot()
    lib.logger.setup_logging(path)

    url = config.get_url_forecast()
    print(url)
    openweather = Openweather(url)
    openweather.parse_data()
    openweather.save_parsed_data_to_json_file(config.get_path_prot())
    

if __name__ == "__main__":
    
    main()
