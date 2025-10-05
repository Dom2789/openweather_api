import api_call 
from lib.Config import Config

def main():
    
    config = Config("/Users/dom/prog/openweather_api/config/config.txt")
    print(config.get_url_forecast())
    
    #api_call.get_posts()


if __name__ == "__main__":
    
    main()
