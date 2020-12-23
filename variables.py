DIRECTIONS = [
    {
        'from': 'ALA',
        'to': 'TSE'
    },
    {
        'from': 'TSE',
        'to': 'ALA'
    },
    {
        'from': 'ALA',
        'to': 'MOW'
    },
    {
        'from': 'MOW',
        'to': 'ALA'
    },
    {
        'from': 'ALA',
        'to': 'CIT'
    },
    {
        'from': 'CIT',
        'to': 'ALA'
    },
    {
        'from': 'TSE',
        'to': 'MOW'
    },
    {
        'from': 'MOW',
        'to': 'TSE'
    },
    {
        'from': 'TSE',
        'to': 'LED'
    },
    {
        'from': 'LED',
        'to': 'TSE'
    }
]
FLIGHTS_URL = 'https://api.skypicker.com/flights' \
              '?fly_from={}' \
              '&fly_to={}' \
              '&date_from={}' \
              '&date_to={}' \
              '&adults=1' \
              '&partner=picky'
CHECK_FLIGHTS_URL = 'https://booking-api.skypicker.com/api/v0.1/check_flights' \
                    '?v=2' \
                    '&booking_token={}' \
                    '&bnum=3' \
                    '&pnum=1' \
                    '&currency=EUR' \
                    '&adults=1'
QUERY_SCHEMA = {
    'from': {
        'type': 'string',
        'required': True
    },
    'to': {
        'type': 'string',
        'required': True
    },
    'date': {
        'type': 'string',
        'required': True
    }
}
FAILURE_MESSAGE = {
    'message': 'There is no flights on this dates or wrong date!'
}
