import redis

r = redis.StrictRedis('localhost',6379, 0)
r.set('foo','bar')

print r.get('foo')