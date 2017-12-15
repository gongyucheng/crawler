import redis
MYSQL_HOST = "192.168.1.170"  #mysql数据库地址
MYSQL_DBNAME = "mianmo"		#数据库表明
MYSQL_USER = "root"			#数据库账户名
MYSQL_PASSWORD = "123456"	#数据库密码
MYSQL_PORT = 3306
MEILI_PRODUCT_TABLE_NAME = "meiliProduct"
MEILI_INGREDIENT_TABLE_NAME = "meiliIngredient"
WATSONS_PRODUCT_TABLE_NAME = "watsons"
LEFENG_PRODUCT_TABLE_NAME = "lefeng"

SPLASH_URL = 'http://localhost:8050'	#splash地址，需要启动容器，修改响应的地址

REDIS_HOST = '192.168.1.88'				#redis 地址
REDIS_PORT = 6379
REDIS_PASSWORD = "okoer.2016"
REDIS_DATABASE_NAME = 1         #redis database_name
REDIS_MEILI_URL_KEY = "meilixiuxing_url" #美丽修行redis存储已爬取url的key
REDIS_LEFENG_URL_KEY = "lefeng_url"      #乐峰redis存储已爬取url的key
REDIS_WATSONS_URL_KEY = "watsons_url"    #屈臣氏redis存储已爬取url的key

#连接redis
redis_db = redis.Redis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DATABASE_NAME,password=REDIS_PASSWORD)