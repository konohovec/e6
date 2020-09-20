import os
import logging

from fastapi import FastAPI
import redis

from utils import fib


app = FastAPI()
logger = logging.getLogger('api-logger')
logger.setLevel(logging.INFO)

redis_config = {
    'host':  os.environ.get('REDIS_HOST'),
    'port': os.environ.get('REDIS_PORT'),
    'db': 0,
}
redis = redis.StrictRedis(**redis_config)


@app.get('/fibonacci/')
def fibonacci(k: int):
    logging.info('')
    res, err = None, None

    if 0 <= k <= 12000:
        res = redis.get(str(k))
        if res:
            logger.info(' GET DATA FROM REDIS')
            res = int(res)
        else:
            logger.info(' CALCULATING NEW VALUE')
            res = fib(k)
            redis.set(str(k), res)
    else:
        err = 'Wrong value. Must be 0<=k<=12000'
        logger.info(f' GOT WRONG ARGUMENT <{k}>')

    return {'res': res, 'error': err}
