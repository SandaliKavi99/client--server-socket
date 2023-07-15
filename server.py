import socket
import threading
import sys


# thread for sent msgs
def createTread(clientSocket,address):
 
   while True:
      print("client ",address,">")
      msg =clientSocket.recv(256).decode()
      if(msg == 'terminate'):
         break
      print(msg)

# make server
def startServer(port):
   server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   server.bind((socket.gethostname(),port))
   server.listen()

   while True:
      clientSocket, address = server.accept()
      print(f"Connection established from address {address}")
      clientSocket.send(bytes("Welcome to the Server!!!!","utf-8"))
      
      threading.Thread(target=createTread,args=(clientSocket,address)).start()

# main function
if __name__ == "__main__":
   if len(sys.argv) != 2:
      print("Usage: py server.py <port>")
      sys.exit(1)
   port = int(sys.argv[1])
   startServer(port)
