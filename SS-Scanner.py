import socket
import os

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")
	os.system("figlet SS-Scaner")

print("Author:   Necracker")
print("Telegram: @necracker")
print("")

# Set socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def portScan():
	host = input("Enter site's IP: ")
	port = int(input("Enter site's port: "))
	print("")
	if s.connect_ex((host, port)):
		print("Port " + str(port) + " - is closed")
	else:
		print("Port " + str(port) + " - is open")
	print("")
	print("")
	main()

def getIP():
	domain = str(input("Enter site's address: "))
	ip = socket.gethostbyname(domain)
	print("")
	print(ip)
	print("")
	print("")
	main()

def main():
	print("1. Check port")
	print("")
	print("2. Get site's IP")
	print("")
	print("3. Exit")
	print("")
	choose = int(input("--> "))
	if choose == 1:
		portScan()
	elif choose == 2:
		getIP()
	elif choose == 3:
		pass
	else:
		print("Choose right option!")
		main()
main()