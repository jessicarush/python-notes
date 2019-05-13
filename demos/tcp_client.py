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
