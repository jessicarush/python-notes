'''Networks and Distributed Computing'''

# Patterns --------------------------------------------------------------------

# You can build networking applications from some basic patterns. The most
# common pattern in request-reply aka client-server. This pattern in
# synchronous in that the client waits for a server response.

# Another common pattern is push or fanout. This is where you send data to any
# available worker in a pool of processes. An example is a web server behind a
# 'load balancer'.

# The opposite pattern to this is pull or fanin which accepts data from one or
# more sources. An example would be a logger that takes messages from multiple
# sources and writes then to a single file. Another pattern is...

# Publish-Subscribe Model -----------------------------------------------------

# With this pattern, a publisher sends out data. In a simple pub-sub system,
# all subscribers would receive all the data, but more commonly, subscribers
# choose which data to receive (topics). Unlike the push pattern, more that one
# subscriber might receive a given piece of data. If there's no subscriber,
# the data is ignored. Publish-Subscribe is not a queue but a broadcast.
# Here's an example using Redis:

# redis_pub.py:
import random
import redis

conn = redis.Redis()
cats = ['siamese', 'black', 'persian', 'main coon', 'tabby', 'norwegian']
hats = ['bowler', 'fedora', 'top hat', 'poor boy', 'cowboy', 'stovepipe']

for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print('Publish: {} cat wears a {}'.format(cat, hat))
    conn.publish(cat, hat)


# redis_sub.py:
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

# The listen method returns a dictionary. If its type is 'message', it was sent
# by the publisher and matches our criteria. The 'channel' key is the topic
# (cat) and the data key contains the message (hat).

# to test, start the subscriber first, then the publisher.

# $ python3 redis_sub.py &
# $ python3 redis_pub,py

# Publish: tabby cat wears a cowboy
# Publish: persian cat wears a poor boy
# Publish: tabby cat wears a top hat
# Publish: black cat wears a cowboy
# Publish: siamese cat wears a top hat
# Subscribe: b'black' cat wears a b'cowboy'
# Publish: siamese cat wears a fedora
# Subscribe: b'siamese' cat wears a b'top hat'
# Publish: persian cat wears a cowboy
# Subscribe: b'siamese' cat wears a b'fedora'
# Publish: tabby cat wears a stovepipe
# Publish: persian cat wears a cowboy
# Publish: tabby cat wears a stovepipe

# Other pub-sub tools ---------------------------------------------------------

# RabbitMQ – https://www.rabbitmq.com
# Pika API – https://pika.readthedocs.io/en/0.10.0/
# Tutorial – http://bit.ly/pub-sub-tut
# pubsubhubbub – https://github.com/pubsubhubbub/

# https://pypi.python.org/pypi?%3Aaction=search&term=pubsub&submit=search
