from http import server
import ADXL345
from i2c_adxl345 import *
import sys
import socket
import time



#Methods

def Main():
    #Property
    ReceiveDataBudder = 2
    #init IP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind the socket to the port
    server_address = ("192.168.0.95",9999)
    print('-->starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    _adx = i2c_adxl345(1)

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
                    time.sleep(0.1)
                    (roll,pitch) = _adx.RollPitch()
                    data = str(roll) + "-" + str(pitch)
                    connection.sendall(data.encode('utf-8'))
                else:
                    print(sys.stderr, '-->no more data from', client_address)
                    break
                
        finally:
            connection.close()
            print("Over!!!")
            break

if __name__ == "__main__":
    Main()