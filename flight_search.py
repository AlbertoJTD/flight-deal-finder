import requests

TEQUILA_ENDPOINT = ""
TEQUILA_API_KEY = ""

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def update_iataCode(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {'apikey': TEQUILA_API_KEY}
        query = {'term': city_name, 'location_types': 'city'}

        response = requests.get(url=location_endpoint, headers=headers, params=query).json()
        code = response['locations'][0]['code']
        return code
