import redis

host = '47.97.213.17'
port = 6379
#这里替换为实例password
pwd = 'r-bp17f80de892ecb4:Ghrhome2009'
r = redis.Redis(host=host, port=port, password=pwd)
#conn = redis.Redis(host='47.97.213.17',port=6379,db=0)
r.set('foo', 'barx');
print(r.get('foo'))