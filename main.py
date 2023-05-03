from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

# GET INFO FROM GOOGLE SHEETS - BASIC AUTH

SHEETY_USERNAME = ''
SHEETY_PASSWORD = ''
ORIGIN_CITY_CODE = 'MEX'

data_manager = DataManager(SHEETY_USERNAME, SHEETY_PASSWORD)
sheet_data = data_manager.get_data()['prices']

flight_search = FlightSearch()
notification_manager = NotificationManager()

for data in sheet_data:
    if not data['iataCode']:
        data['iataCode'] = flight_search.get_iataCode(data['city'])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_months_in_the_future = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(origin_city_code=ORIGIN_CITY_CODE,
                                         destination_city_code=destination['iataCode'],
                                         from_time=tomorrow,
                                         to_time=six_months_in_the_future)

    if flight is not None and flight.price < destination['lowestPrice']:
        message = f'Only USD: ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}'
        notification_manager.send_email(message)
