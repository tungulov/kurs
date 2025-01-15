import json
import os
import redis


redis_host = 'redis' if os.getenv('PROD') == "True" else '127.0.0.1'

r = redis.from_url(f'redis://{redis_host}:{os.getenv('REDIS_PORT')}')