import socket
import sys
import serial
import struct

#from numpy import roll

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("192.168.0.95", 9999)
print('>> connecting to %s port %s' % server_address)
sock.connect(server_address)
Respondmes = "."

ser = serial.Serial()

try:
    rollF = None
    pitchF = None
    yawF = None
    ser.port = "COM1"
    ser.baudrate = 9600
    ser.timeout = 1
    if ser.is_open:
        print("COM1 IS BUSY!")
        sock.close()
        sys.exit()
    ser.open()
    while True:
        sock.sendall(Respondmes.encode('utf-8'))
        # Look for the response
        data = sock.recv(1024)
        print('>> received "%s"' % data.decode("utf-8"))
        receivedatasplit = data.decode('utf-8').split('$$')
        print(receivedatasplit[0])
        print(receivedatasplit[1])
        _roll = float(receivedatasplit[0])
        _pitch = float(receivedatasplit[1])
        _yaw = float(receivedatasplit[2])
        if(rollF == None):
            rollF = _roll
            pitchF = _pitch
            yawF = _yaw
        else:
            rollF = 0.94 * rollF + 0.06 * _roll
            pitchF = 0.94 * pitchF + 0.06 * _pitch
            yawF = 0.94 * yawF + 0.06 * _yaw
        senddata = str(rollF) + "/" + str(pitchF) + str(yawF) + "\n"
        ser.write(senddata.encode("ASCII"))
except Exception as e:
    print(str(e))

finally:
    print(sys.stderr, '>> closing socket')
    if ser.is_open:
        ser.close()
    sock.close()