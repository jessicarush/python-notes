import random
import redis

conn = redis.Redis()
cats = ['siamese', 'black', 'persian', 'main coon', 'tabby', 'norwegian']
hats = ['bowler', 'fedora', 'top hat', 'poor boy', 'cowboy', 'stovepipe']

for i in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print('Publish: {} cat wears a {}'.format(cat, hat))
    conn.publish(cat, hat)
