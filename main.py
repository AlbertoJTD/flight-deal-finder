#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests

from data_manager import DataManager

# GET INFO FROM GOOGLE SHEETS - BASIC AUTH

sheet_endpoint = ''
SHEETY_USERNAME = ''
SHEETY_PASSWORD = ''


sheet_data = DataManager(SHEETY_USERNAME, SHEETY_PASSWORD, sheet_endpoint,).get_data()
print(sheet_data)