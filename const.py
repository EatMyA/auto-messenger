import redis

XSRF_COOKIE = 'XSRF-TOKEN'
LARAVEL_COOKIE = 'laravel_session'

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
CACHE_XSRF_EXPIRE = 2*60*59
CACHE_LARAVEL_EXPIRE = 23*60*59
CACHE_KEY_MEMBERS = 'members'
