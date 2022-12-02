#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


data_manage = DataManager()
flight_sea = FlightSearch()
notify = NotificationManager()

sheet_data = data_manage.read()

for i in sheet_data:
    if i['iataCode'] == '':
        iata = flight_sea.check_iata_code(i['city'])
        i['iataCode'] = iata

# Updates airport IATA code.
data_manage.update_iata_code()

for i in sheet_data:
    flight_DATA = FlightData('LON', i['iataCode'])
    price = flight_DATA.search_flight()
    if price <= i['lowestPrice']:
        print(f"day is: {flight_DATA.end_day}")
        notify.alert('London', 'LON', i['city'], i['iataCode'], price, flight_DATA.start_day, flight_DATA.start_month,
                     flight_DATA.start_year, flight_DATA.end_day, flight_DATA.end_month, flight_DATA.end_year)





