from data_manager import DataManager
from notification_manager import NotificationManager


class FlightData:

    def __init__(self, **kwargs):
        self.price = kwargs['price']
        self.origin_city = kwargs['origin_city']
        self.origin_airport = kwargs['origin_airport']
        self.destination_city = kwargs['destination_city']
        self.destination_airport = kwargs['destination_airport']
        self.out_date = kwargs['out_date']
        self.return_date = kwargs['return_date']
        self.stop_overs = kwargs['stop_overs']
        self.via_city = kwargs['via_city']

    def is_cheap_flight(self):
        data_manager = DataManager()

        notification_manager = NotificationManager()

        notification_manager.send_text(
            price=self.price,
            origin_city=self.origin_city,
            origin_airport=self.origin_airport,
            destination_city=self.destination_city,
            destination_airport=self.destination_airport,
            out_date=self.out_date,
            return_date=self.return_date,
            stop_over=self.stop_overs,
            via_city=self.via_city
        )

