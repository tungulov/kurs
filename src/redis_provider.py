import json
import os
import redis


redis_host = 'redis' if os.getenv('PROD') == "True" else '127.0.0.1'

r = redis.from_url(f'redis://{redis_host}:{os.getenv('REDIS_PORT')}')

def get_ships_redis():
    ships = r.get('ships')
    if ships:
        return json.loads(ships)

def set_ships_redis(ships):
    for ship in ships['data']:
        ship['date'] = ship['date'].strftime('%Y-%m-%d')

    ships_str = json.dumps(ships)
    r.set('ships', ships_str)