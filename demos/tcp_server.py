import datetime
import socket


address = ('localhost', 4544)
max_size = 1000  # bytes
print('Starting the server at', datetime.datetime.now())
print('waiting for client to call')

# SOCK_DGRAM is replaced with SOCK_STREAM to use the streaming TCP protocol:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

# This queues up to 5 client connections before refusing new ones:
server.listen(5)

# TCP gets the first available message as it arrives:
client, addr = server.accept()
data = client.recv(max_size)
print('Message:', datetime.datetime.now(), client, 'said', data)

client.sendall(b'Are you talking to me?')
client.close()
server.close()
