import asyncio
import datetime
import pickle

from dateutil.relativedelta import relativedelta
from huey import crontab, RedisHuey
from pip._vendor import requests

from manage import cache
from utils import check_to_valid
from variables import DIRECTIONS, FLIGHTS_URL


huey = RedisHuey()


@huey.periodic_task(crontab(hour='0'))
def parse_directions():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for direction in DIRECTIONS:
        flights = []
        date_start = datetime.datetime.now().date()
        date_end = date_start + relativedelta(months=+1)
        delta = date_end - date_start
        for i in range(delta.days + 1):
            day = date_start + datetime.timedelta(days=i)
            day = day.strftime('%d/%m/%Y')
            req = requests.get(FLIGHTS_URL.format(direction['from'], direction['to'], day, day))
            data = sorted(req.json()['data'], key=lambda k: k['price'])
            if data:
                res = loop.run_until_complete(check_to_valid(data))
                flights.append(res)
            cache.set('{}_{}'.format(direction['from'], direction['to']), pickle.dumps(flights), 24*60*60)

