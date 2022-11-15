from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.account_sid = 'TWILIO_SSID'
        self.auth_token = 'TWILIO_AUTH_TOKEN'

    def send_text(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                  return_date, stop_over, via_city):
        if stop_over != 0:
            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                body=f'Low price alert! Only ${price} to fly from {origin_city}-{origin_airport} to '
                     f'{destination_city}-{destination_airport}, from {out_date} to {return_date}.\n '
                     f'Flight has {stop_over} layover, via {via_city}.',
                from_='+11234567890',
                to='+11234567890'
            )
        else:
            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                body=f'Low price alert! Only ${price} to fly from {origin_city}-{origin_airport} to '
                 f'{destination_city}-{destination_airport}, from {out_date} to {return_date}.',
                from_='+11234567890',
                to='+11234567890'
            )
