from http import server
import ADXL345
import sys
import socket
import time



#Methods

def Main():
    #Property
    ReceiveDataBudder = 1024
    #init IP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind the socket to the port
    server_address = ("192.168.0.95",9999)
    print('-->starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    _adx = ADXL345.ADXL345(1)

    while True:
        # Wait for a connection
        print('-->waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('-->connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(ReceiveDataBudder)
                if data:
                    print("-->Client Required!")
                    (roll,pitch) = _adx.RollPitch()
                    data = ""
                    print("--> Send: " + data)
                    data = str(roll) + "-" + str(pitch)
                    print("--> Send: " + data)
                    connection.sendall(data)
                else:
                    print(sys.stderr, '-->no more data from', client_address)
                    break
                
        finally:
            connection.close()
            print("Over!!!")
            break

if __name__ == "__main__":
    Main()