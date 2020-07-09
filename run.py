import os


os.system("start server_0.py 127.0.0.1 66")	
while True:
	os.system("start client_0.py 127.0.0.1 66")

	exit = input("Add more? Y or N : ")
	if exit == 'N' or exit == 'n':
		break
