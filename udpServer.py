import socket

localIP = "127.0.0.1"
localPort = 9997
bufferSize = 1024

serverSocker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind  address & ip
serverSocker.bind((localIP, localPort))

print("UDP server up and listening")

# Listen
while(True):
    bytesAddressPair = serverSocker.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Pesan Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    serverSocker.sendto(b"Selamat datang di UDP Server", address)