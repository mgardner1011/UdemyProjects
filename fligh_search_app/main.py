from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta


data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(6 * 30))

for row in sheet_data:
    flight_search.city_code = row['iataCode']
    flight_search.price = row['lowestPrice']
    flight_search.tomorrow = tomorrow.strftime('%d/%m/%Y')
    flight_search.six_months_from_now = six_months_from_now.strftime('%d/%m/%Y')

    flights = flight_search.check_flights()

    try:
        if flights.price < row['lowestPrice']:
            flights.is_cheap_flight()
    except AttributeError:
        pass


