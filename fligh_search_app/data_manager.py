import requests

SHEET_ENDPOINT = 'SHEETY_ENDPOINT'


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        self.destination_data = response.json()
        return self.destination_data['prices']

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data
            )
