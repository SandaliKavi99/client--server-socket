import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((socket.gethostname(),6040))

message = client.recv(2048)

print(f"Message recived: {message}")