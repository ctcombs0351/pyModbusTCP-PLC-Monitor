import socket

HEADER = 10
SERVER = 'localhost'
PORT = 1234
ADDR = (SERVER, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f'Connection from {address} has been established')
	
	msg = 'Welcome to the Server'
	msg = f'{len(msg):<{HEADER}}' + msg

	clientsocket.send(bytes(msg, 'utf-8'))
