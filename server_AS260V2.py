import socket 
import threading

PORT = 1234
SERVER = 'localhost'
ADDR = (SERVER, PORT)
HEADER = 10
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'Fuck Off'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f'[NEW CONNECTION] {addr} connected.')
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False
			print(f'[{addr}] {msg}')
	conn.close()

def start():
	server.listen(5)
	print(f'[LISTENING]  Server is listening on {SERVER}')
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target = handle_client, args = (conn, addr))
		thread.start()
		print(f'[ACTIVE CONNECTIONS] {threading.activeCount() -1}')

print('(STARTING) server is starting...')
start()
 
