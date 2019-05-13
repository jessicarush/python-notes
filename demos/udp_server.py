import datetime
import socket


server_address = ('localhost', 4544)
max_size = 4096
print('Starting the server at', datetime.datetime.now())
print('waiting for client to call')

# This line creates a socket (AF_INET means we'll create an IP socket,
# SOCK_DGRAM means we'll send and receive datagrams - UDP):
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# This listens for any data arriving at the IP, port. The programs sits and
# waits here until there's some action:
server.bind(server_address)

# Any data that comes in will be received here:
data, client = server.recvfrom(max_size)
print('Message:', datetime.datetime.now(), client, 'said', data)

# The server sends a reply:
server.sendto(b'Are you talking to me?', client)

# and closes the connection:
server.close()
