'''Networks and Distributed Computing'''

# -----------------------------------------------------------------------------
# Patterns
# -----------------------------------------------------------------------------
# You can build networking applications from some basic patterns. The most
# common pattern in request-reply aka client-server. This pattern in
# synchronous in that the client waits for a server response.

# Another common pattern is push or fanout. This is where you send data to any
# available worker in a pool of processes. An example is a web server behind a
# 'load balancer'.

# The opposite pattern to this is pull or fanin which accepts data from one or
# more sources. An example would be a logger that takes messages from multiple
# sources and writes then to a single file. Another pattern is...

# -----------------------------------------------------------------------------
# Publish-Subscribe Model
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# Other pub-sub tools
# -----------------------------------------------------------------------------
# RabbitMQ – https://www.rabbitmq.com
# Pika API – https://pika.readthedocs.io/en/0.10.0/
# Tutorial – http://bit.ly/pub-sub-tut
# pubsubhubbub – https://github.com/pubsubhubbub/

# https://pypi.python.org/pypi?%3Aaction=search&term=pubsub&submit=search

# -----------------------------------------------------------------------------
# TCP/IP
# -----------------------------------------------------------------------------
# In the middle of the stack layers of protocols that handle our internet
# connections, data exchanges and so on, is the IP protocol layer which
# specifies how network locations are addressed and how packets of data flow.
# Your local machine always has the IP address 127.0.0.1 and the name localhost.
# If it's connect to the internet, it will also have a public IP address. In the
# layer above the IP protocol, two protocols describe how to move bytes between
# locations:

# UDP – (user datagram protocol) used for short exchanges. A tiny message sent
# in a single burst with no acknowledgment that the data was received. It's
# fast and light but unreliable in the sense that multiple messages may arrive
# out of order or not at all. Just saying.

# TCP – (transmission control protocol) used for longer-lived connections. It
# send streams of bytes and ensures they arrive in order without duplication.

# Most of the internet with which we interact (web, database servers, etc) is
# based on the TCP protocol running on top of the IP protocol–TCP/IP for short.

# -----------------------------------------------------------------------------
# Sockets
# -----------------------------------------------------------------------------
# A socket is one endpoint of a two-way communication link between two programs
# running on the network. A socket is bound to a port number. An endpoint is a
# combination of an IP address and a port number.

# The following is an example of a simple client-server exchange. The client
# sends a string in UDP datagram to a server and the server returns a packet
# containing a string. In each program we'll print the time and open a socket
# (address and port). The server will listen for connections to its socket.
# The client will write to the socket which transmits the message.

# upd_server.py:
import datetime
import socket

server_address = ('localhost', 4544)
max_size  = 4096
print('Starting the server at', datetime.datetime.now())
print('waiting for client to call')
# This line creates a socket (AF_INET means we'll create an IP socket,
# SOCK_DGRAM means we'll send and receive datagrams - UDP):
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# This listens for any data arriving at the IP, port. The programs sits and
# waits here until theres some action:
server.bind(server_address)
# Any data that comes in will be received here:
data, client = server.recvfrom(max_size)
print('Message:', datetime.datetime.now(), client, 'said', data)
# The server sends a reply:
server.sendto(b'Are you talking to me?', client)
# and closes the connection:
server.close()


# upd_client.py:
import datetime
import socket

server_address = ('localhost', 4544)
max_size = 4096
print('Starting the client at', datetime.datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hello', server_address)
data, server = client.recvfrom(max_size)
print('Message:', datetime.datetime.now(), server, 'said', data)
client.close()

# Note that the client doesn't need a bind, because it's not doing the
# listening. Also, the client needs to know the server address and port but
# doesn't need to specify one for itself...this is automatically assigned by
# the system.

# Here's the same thing but sent via TCP:

# tcp_server.py:
import datetime
import socket

address = ('localhost', 4544)
max_size  = 1000  # bytes
print('Starting the server at', datetime.datetime.now())
print('waiting for client to call')
# SOCK_DGRAM is replaced with SOCK_STREAM to use the streaming TCP protocol:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
# This queues up to 5 client connections before refusing new ones:
server.listen(5)
# Tgi gets the first available message as it arrives:
client, addr = server.accept()
data = client.recv(max_size)
print('Message:', datetime.datetime.now(), client, 'said', data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()

# tcp_client.py:
import datetime
import socket

address = ('localhost', 4544)
max_size = 1000
print('Starting the client at', datetime.datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The connect() call sets up a stream
client.connect(address)
client.sendall(b'Hi there')
data = client.recv(max_size)
print('Message:', datetime.datetime.now(), 'someone replied', data)
client.close()

# -----------------------------------------------------------------------------
# some points to note:
# -----------------------------------------------------------------------------
# – UDP sends messages but their size is limited and not guaranteed to reach
#   their destination.

# – TCP sends streams of bytes, not messages. To send an entire message via TCP
#   you need extra information to reassemble the full message from it's bytes
#   segments (a fixed message size in bytes, the size of the full message, or
#   some delimiting character). Because these are bytes, you need to use the
#   python bytes type (not unicode text strings).

# – ZeroMQ is a good library for working with sockets. Does a bit more:
#   http://zguide.zeromq.org/
