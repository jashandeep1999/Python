import pyfiglet 
import sys 
import socket 
from datetime import datetime 

ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print(ascii_banner) 

# Defining a target 
target = input('Enter ip addr: ')
portrange = (input("Enter port range(0-2000):"))
lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])
# Add Banner 
print("-" * 50) 
print("Scanning Target: " + target) 
print("-" * 50) 

try: 
	
	# will scan ports 
	for port in range(lowport,highport): 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		socket.setdefaulttimeout(1) 
		
		# returns an error indicator 
		result = s.connect_ex((target,port)) 
		if result ==0: 
			print("Port {} is open".format(port)) 
		s.close() 
		
except KeyboardInterrupt: 
		print("\n Exitting Program !!!!") 
		sys.exit() 
except socket.error: 
		print("\ Server not responding !!!!") 
		sys.exit() 
