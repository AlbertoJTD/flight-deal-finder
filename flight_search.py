import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "HERE_GOES_YOUR_API_KEY"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iataCode(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {'apikey': TEQUILA_API_KEY}
        params = {'term': city_name, 'location_types': 'city'}

        response = requests.get(url=location_endpoint, headers=headers, params=params).json()
        code = response['locations'][0]['code']
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = headers = {'apikey': TEQUILA_API_KEY}
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=headers, params=params).json()

        try:
            data = response['data'][0]
        except IndexError:
            print('Sorry: No flights available')
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        return flight_data

