from sanic import Sanic
from sanic.response import json
from redis import Redis
from sanic_validation import validate_args

from variables import QUERY_SCHEMA, FAILURE_MESSAGE

app = Sanic('flights')
app.config.update(
    {
        'REDIS': {
            'address': ('127.0.0.1', 6379),
        }
    }
)

cache = Redis()


@app.route('/flights')
@validate_args(QUERY_SCHEMA)
async def test(request):
    from utils import search_tickets
    query_from = request.args.get('from')
    query_to = request.args.get('to')
    query_date = request.args.get('date')
    result = search_tickets(query_from, query_to, query_date)
    if result:
        return json(result)
    return json(FAILURE_MESSAGE)


if __name__ == "__main__":
  app.run(debug=True, access_log=True)
