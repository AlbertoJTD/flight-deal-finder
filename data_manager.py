import requests

SHEETY_ENDPOINT = 'HERE_GOES_YOUR_ENDPOINT_FROM_SHEETY'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.destination_data = {}

    def get_data(self):
        response = requests.get(SHEETY_ENDPOINT, auth=(self.username, self.password))
        response.raise_for_status()
        return response.json()

    def update_destination_codes(self):
        for city in self.destination_data:
            new_info = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(f"{SHEETY_ENDPOINT}/{city['id']}", json=new_info, auth=(self.username, self.password))
