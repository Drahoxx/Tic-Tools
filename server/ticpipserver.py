#!/usr/bin/python3
import socket
import os
import tqdm
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 2102
BUFFER_SIZE = 4096
s = socket.socket()
try:
	s.bind((SERVER_HOST, SERVER_PORT))
	s.listen(5)
	print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
	while True:
		cs, address = s.accept()
		print(f"[+] {address} is connected.")
		received = cs.recv(BUFFER_SIZE).decode()
		plugin = received
		plugins = map(lambda a: str(a).lower(),os.listdir("./plugins"))
		if plugin.lower()+".py" in plugins:
			cs.send('202'.encode())
			cs.recv(BUFFER_SIZE)
			cs.send(plugin.encode())
			cs.recv(BUFFER_SIZE).decode()
			cs.send(str(os.path.getsize('./plugins/'+plugin+".py")).encode())
			cs.recv(BUFFER_SIZE).decode()

			with open('./plugins/'+plugin+".py", "rb") as f:
				while True:
					bytes_read = f.read(BUFFER_SIZE)
					if not bytes_read:
						print("End ----")
						break
					cs.send(bytes_read)
		else:
			cs.send('404'.encode())
except ValueError as e:
	print(e)
	s.close()