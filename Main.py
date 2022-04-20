from http import server
import ADXL345
import sys
import socket
import time



#Methods

def Main():
    #Property

    #init IP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind the socket to the port
    server_address = ("192.168.0.95",9999)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print('received "%s"' % data.decode('utf-8'))
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print(sys.stderr, 'no more data from', client_address)
                    break
                
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    Main()