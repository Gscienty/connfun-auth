import redis


redis_connetion_pool = redis.ConnectionPool(host=os.getenv('REDIS_HOST'), port=6379)
