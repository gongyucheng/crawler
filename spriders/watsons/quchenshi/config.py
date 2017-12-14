import redis
MYSQL_HOST = "192.168.1.88"
MYSQL_DBNAME = "bang"
MYSQL_USER = "root"
MYSQL_PASSWORD = "yaochizaocan"
MYSQL_PORT = 3306

SPLASH_URL = 'http://localhost:8050'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DATABASE_NAME = 1
REDIS_WATSONS_URL_KEY = "watsons_url"

#redis
redis_db = redis.Redis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DATABASE_NAME)