import requests

URL = 'https://api.sheety.co/39a91da1646e97ce85f01a01c71c427d/club/sheet1'


class DataManager:
    def __init__(self):
        self.flight_data = ''

    def read(self):
        response = requests.get(URL).json()
        self.flight_data = response['sheet1']
        return self.flight_data

    def update_iata_code(self):
        for i in self.flight_data:
            new_data = {
                'sheet1': {
                    'iataCode': i['iataCode']
                }
            }
            requests.put(url=URL + f"/{i['id']}", json=new_data)

