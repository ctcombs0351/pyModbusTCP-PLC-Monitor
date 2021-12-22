import socket

HEADER = 10
SERVER = 'localhost'
PORT = 1234
ADDR = (SERVER, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

full_msg = ''

while True:
	
	full_msg = ''
	new_msg = True
	while True:
		msg = s.recv(16)
		if new_msg:
			print(f'new message length: {msg[:HEADER]}')
			msglen = int(msg[:HEADER])
			new_msg = False
		full_msg += msg.decode('utf-8')

		if len(full_msg) - HEADER == msglen:
			print('Full Message Received')
			print(full_msg[HEADER:])
		new_msg = True
		full_msg = ''
print(full_msg)
