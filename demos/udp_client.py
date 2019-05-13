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
