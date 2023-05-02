import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, username, password, sheet_endpoint):
        self.username = username
        self.password = password
        self.sheet_endpoint = sheet_endpoint

    def get_data(self):
        response = requests.get(self.sheet_endpoint, auth=(self.username, self.password))
        response.raise_for_status()
        return response.json()