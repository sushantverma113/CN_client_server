import socket
import decrypt


#constants
host = socket.gethostname()
print(host)
port = 12345

#opening the socket
s = socket.socket() 

#binding it to the port, "" specifies connection allowed from different systems within same network
s.bind(("", port))			

#setting the socket to listen
s.listen(5)
print("Server Online")

cnt=1

#Whie true specifies that server remains on irrespective
while True:
	#connecting to client
	c, addr = s.accept()
	print('\n****************Client connected : ', addr)

	torec = './toReceive/part'+str(cnt)+'.csv'
	cnt+=1

	#opening a new file to store data
	f = open(torec, mode="wb")


	#recieving file
	print("\nReceiving file ...")
	#recieve packets
	pack = c.recv(1024)
	while (pack):
		f.write(pack)
		pack = c.recv(1024)
	f.close()
	print ("Done Receiving")
	print(cnt)
	#closing the connection to client
	c.close()
	break

decrypt.main()

#closing the socket
s.close()