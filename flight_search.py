import requests

Tequila_URL = 'https://api.tequila.kiwi.com/locations/query?'
Tequila_API = 'pILSQEtm8ntNLtu1LbAAoi5HWJYUdL1K'


class FlightSearch:

    def check_iata_code(self, city_name):
        header = {
            'apikey': Tequila_API
        }
        data = {
            'term': city_name
        }
        response = requests.get(Tequila_URL, headers=header, params=data)
        return response.json()['locations'][0]['code']


