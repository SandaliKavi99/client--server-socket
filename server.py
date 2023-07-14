import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((socket.gethostname(),6040))
server.listen()

while True:
   clientSocket, address = server.accept()
   print(f"Connection established from address {address}")
   clientSocket.send(bytes("Welcome to the Server!!!!","utf-8"))
   clientSocket.close()