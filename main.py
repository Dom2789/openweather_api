from lib.Config import config
from lib.API_handler import api_handler

def main():   
    url = config.get_url_forecast()
    print(url)
    print(api_handler.parse_data(url))


if __name__ == "__main__":
    
    main()
