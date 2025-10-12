from lib.Config import config
from Openweather import Openweather
import lib.logger

def main():  
    path = config.get_path_prot()
    lib.logger.setup_logging(path)

    url = config.get_url_forecast()
    print(url)
    openweather = Openweather(url)
    print(openweather.parse_data())


if __name__ == "__main__":
    
    main()
