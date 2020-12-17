import socket
import split_encrypt


split_encrypt.main("data.csv")


#constants
port = 12345
# host = socket.gethostname()
host = ""
print(host)

#Creating a socket and connecting to server
s = socket.socket()
s.connect((host, port))


for cnt in range(3):

	tosend = '.\toSend\part' + str(cnt+1) + '.csv'

	#opening file to send
	f = open(tosend,'rb')
	#Sending file to compress
	print ('\n Sending file parts...')
	pack = f.read(1024)
	while(pack):
		s.send(pack)
		pack = f.read(1024)
	f.close()
	print ("Done Sending file-part")


#Shutting down the sending capabilities of client socket
s.shutdown(socket.SHUT_WR)
# Closing the socket
s.close()