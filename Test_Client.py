import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("192.168.0.95", 9999)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
Respondmes = "."
try:
    
    print(sys.stderr, 'sending "%s"' % Respondmes)
    sock.sendall(Respondmes.encode('utf-8'))
    # Look for the response
    data = sock.recv(20)
    print(sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()