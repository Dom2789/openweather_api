import requests

class API_handler():

    def __init__(self):
        self.data = None
        self.parsed = {}


    @staticmethod
    def get_posts(url:str):
        try:
            # Make a GET request to the API endpoint using requests.get()
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                posts = response.json()
                return posts
            else:
                print('Error:', response.status_code)
                return None
            
        except requests.exceptions.RequestException as e:
            # Handle any network-related errors or exceptions
            print('Error:', e)
            return None
        
    
    def parse_data(self, url:str):
        self.data = self.get_posts(url)
        # method to parse data
        # current weatherdata + 3 more datasets
        # city, sunset, sunrise, coordinates
        if self.data is None:
            return None
        else:
            self.parsed['now'] = self.data['list'][0]

            return self.parsed
        

api_handler = API_handler()   