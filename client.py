import socket
import sys

def startClient(host,port):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((socket.gethostname(),port))

    message = client.recv(2048)
    print(f"Message recived: {message}")
    while True:
        msg = input('Enter a message: ')
        client.send(msg.encode('utf-8'))
        if(msg == 'terminate'):
            client.close()
            break
    

# main function
if __name__ == "__main__":
   if len(sys.argv) != 3:
      print("Usage: py server.py <server IP> <port>")
      sys.exit(1)
   serverIP = sys.argv[1]
   port = int(sys.argv[2])
  

   startClient(serverIP,port)