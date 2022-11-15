import requests
from flight_data import FlightData
import time


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "TEQUILA_API_KEY"


class FlightSearch:
    def __init__(self):
        self.headers = {
            'apikey': TEQUILA_API_KEY
        }
        self.departure_city = 'MKC'
        self.city_code = ''
        self.price = 0
        self.tomorrow = ''
        self.six_months_from_now = ''

    def get_destination_code(self, city_name):

        endpoint = f'{TEQUILA_ENDPOINT}/locations/query'

        params = {
            'term': city_name,
            'locale': 'en-US',
            'location_types': 'city',
        }

        response = requests.get(url=endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        code = data['locations'][0]['code']
        return code

    def check_flights(self):
        headers = {
            'apikey': TEQUILA_API_KEY
        }

        params = {
            'fly_from': self.departure_city,
            'fly_to': self.city_code,
            'date_from': self.tomorrow,
            'date_to': self.six_months_from_now,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'curr': 'USD',
            'locale': 'en',
            'stop_overs': 1,
            'sort': 'price',
            'asc': 1
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}/search', params=params, headers=headers)
        response.raise_for_status()

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights found for {self.city_code}')
            return None

        if len(data['route']) < 4:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                stop_overs=0,
                via_city='',
                out_date=time.strftime('%Y-%m-%d', time.localtime(data['route'][0]['dTime'])),
                return_date=time.strftime('%Y-%m-%d', time.localtime(data['route'][1]['dTime']))
            )
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                stop_overs=1,
                via_city=data['route'][0]['cityTo'],
                out_date=time.strftime('%Y-%m-%d', time.localtime(data['route'][0]['dTime'])),
                return_date=time.strftime('%Y-%m-%d', time.localtime(data['route'][2]['dTime']))
            )
        return flight_data



# time.strftime('%Y-%m-%d', time.localtime(data['route'][0]['dTime']))
