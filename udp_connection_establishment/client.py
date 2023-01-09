import socket

clt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

clt.sendto("This is UDP client".encode(),('localhost',15000))

msg,address=clt.recvfrom(1024)
print(msg)
