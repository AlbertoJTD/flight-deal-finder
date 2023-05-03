#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

from data_manager import DataManager
from flight_search import FlightSearch

# GET INFO FROM GOOGLE SHEETS - BASIC AUTH

SHEETY_USERNAME = ''
SHEETY_PASSWORD = ''


data_manager = DataManager(SHEETY_USERNAME, SHEETY_PASSWORD)
sheet_data = data_manager.get_data()['prices']

flight_search = FlightSearch()

for data in sheet_data:
    if not data['iataCode']:
        data['iataCode'] = flight_search.update_iataCode(data['city'])


print(sheet_data)
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()
