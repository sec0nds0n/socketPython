import socket

targetHost = "www.google.com"
targetPort = 80

#membuat socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((targetHost, targetPort))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#menangkap respon
respon = client.recv(4096)
print(respon.decode())

client.close()