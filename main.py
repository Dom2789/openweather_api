from lib.Config import Config
from lib.API_handler import API_handler

def main():
    
    config = Config("/Users/dom/prog/openweather_api/config/config.txt")
    url = config.get_url_forecast()
    print(url)

    data = API_handler.get_posts(url)

    print(data["city"])


if __name__ == "__main__":
    
    main()
