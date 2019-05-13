import redis

conn = redis.Redis()
print('Washer is starting')
dishes = ['salad', 'bread', 'main', 'side', 'dessert']

for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('washed', dish)

conn.rpush('dishes', 'quit')
print('Washer is done')
