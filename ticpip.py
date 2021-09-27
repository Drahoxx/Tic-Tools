#!/usr/bin/python3
from sys import argv
import socket
import os
import tqdm
BUFFER_SIZE = 4096
host = 'localhost'
port = 2102

print(r"""__/\\\\\\\\\\\\\\\______________________/\\\\\\\\\\\\\_______________________        
 _\///////\\\/////______________________\/\\\/////////\\\_____________________       
  _______\/\\\________/\\\_______________\/\\\_______\/\\\__/\\\___/\\\\\\\\\__      
   _______\/\\\_______\///______/\\\\\\\\_\/\\\\\\\\\\\\\/__\///___/\\\/////\\\_     
	_______\/\\\________/\\\___/\\\//////__\/\\\/////////_____/\\\_\/\\\\\\\\\\__    
	 _______\/\\\_______\/\\\__/\\\_________\/\\\_____________\/\\\_\/\\\//////___   
	  _______\/\\\_______\/\\\_\//\\\________\/\\\_____________\/\\\_\/\\\_________  
	   _______\/\\\_______\/\\\__\///\\\\\\\\_\/\\\_____________\/\\\_\/\\\_________ 
		_______\///________\///_____\////////__\///______________\///__\///__________

""")
if len(argv)<3:
	print("install or uninstall <plugin_name>")
	exit()

if argv[1].lower() == 'install': 
	s = socket.socket()
	print(f"[+] Connecting to {host}:{port}")
	s.connect((host, port))
	print("[+] Connected.")
	s.send(argv[2].encode())
	code = int(s.recv(BUFFER_SIZE).decode())
	print(code)
	if code==202:
		print("[+] Start downloading the plugin")
		s.send("ok".encode())
		plugin =s.recv(BUFFER_SIZE).decode()
		print(f"[i] Plugin : {plugin}")
		s.send("ok".encode())
		filesize=int(s.recv(BUFFER_SIZE).decode())
		print(f"[i] File size : {filesize}")
		s.send("ok".encode())

		progress = tqdm.tqdm(range(filesize), f"Receiving {plugin}.py", unit="B", unit_scale=True, unit_divisor=1024)
		with open(f"./plugins/{argv[2].lower()}.py", "wb") as f:
			while True:
				bytes_read = s.recv(BUFFER_SIZE)
				if len(bytes_read)<BUFFER_SIZE:
					f.write(bytes_read)
					break
				f.write(bytes_read)
				progress.update(len(bytes_read))
		print("[+] It's done ! Enjoy")
	elif code==404:
		print("[X] We didnt find this plugin")
	else:
		print("[X] Error")
elif argv[1].lower() == 'uninstall':
	try:
		os.remove(f"./plugins/{argv[2]}.py")
		print('It has been uninstall')
	except:
		print('Something went wrong...')