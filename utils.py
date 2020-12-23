import datetime
import pickle

from pip._vendor import requests

from manage import cache
from variables import CHECK_FLIGHTS_URL


def search_tickets(fly_from, fly_to, date):
    data = cache.get('{}_{}'.format(fly_from, fly_to))
    res = pickle.loads(data)
    for flight in res:
        if flight['fly_date'] == date:
            return flight
    return None


async def check_to_valid(data):
    result = {}
    for flight in data:
        req = requests.get(CHECK_FLIGHTS_URL.format(flight['booking_token']))
        request = req.json()
        while not request['flights_checked']:
            req = requests.get(CHECK_FLIGHTS_URL.format(flight['booking_token']))
            request = req.json()
        if not request['flights_invalid']:
            result = {
                'from': flight['flyFrom'],
                'to': flight['flyTo'],
                'fly_date': datetime.datetime.fromtimestamp(flight['dTimeUTC']).strftime('%d-%m-%Y'),
                'fly_start': datetime.datetime.fromtimestamp(flight['dTimeUTC']).strftime('%d.%m.%Y, %H:%M'),
                'fly_end': datetime.datetime.fromtimestamp(flight['aTimeUTC']).strftime('%d.%m.%Y, %H:%M'),
                'fly_duration': flight['fly_duration'],
                'price': '{} {}'.format((request['flights_price']
                                         if request['price_change'] == 'true'
                                         else flight['price']),
                                        request['currency'])
            }
            break
    return result
