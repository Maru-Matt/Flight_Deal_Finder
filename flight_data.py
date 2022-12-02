import requests
from datetime import *

Tequila_URL = 'https://api.tequila.kiwi.com/v2/search?'
Tequila_API = 'pILSQEtm8ntNLtu1LbAAoi5HWJYUdL1K'


class FlightData:
    def __init__(self, city_from, city_to):
        self.city_from = city_from
        self.city_to = city_to
        self.start_day = ''
        self.end_day = ''
        self.start_month = ''
        self.start_year = ''
        self.end_month = ''
        self.end_year = ''
        self.flight_time()

    def flight_time(self):
        self.start_day = str(datetime.now() + timedelta(1)).split('-')[2].split(" ")[0]
        self.start_month = str(datetime.now()).split("-")[1]
        self.start_year = str(datetime.now()).split("-")[0]
        self.end_day = str(datetime.now() + timedelta(180)).split('-')[2].split(" ")[0]
        self.end_month = str(datetime.now() + timedelta(180)).split('-')[1]
        self.end_year = str(datetime.now() + timedelta(180)).split('-')[0]

    def search_flight(self):
        temp = []
        head = {
            'apikey': Tequila_API
        }
        data = {
            'fly_from': self.city_from,
            'fly_to': self.city_to,
            'data_from': f'{self.start_day}{self.start_month}{self.start_year}',
            'data-to': f'{self.end_day}{self.end_month}{self.end_year}',
            'curr': 'GBP',
            'nights_in_dst_from': 2,
            'nights_in_dst_to': 3
        }
        response = requests.get(Tequila_URL, headers=head, params=data)
        temp.append(response.json()['data'][0]['price'])
        return response.json()['data'][0]['price']

