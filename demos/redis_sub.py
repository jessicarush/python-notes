import redis

conn = redis.Redis()
topics = ['siamese', 'black']
sub = conn.pubsub()
sub.subscribe(topics)

for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print('Subscribe: {} cat wears a {}'.format(cat, hat))
