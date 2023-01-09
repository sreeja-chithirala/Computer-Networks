import socket

clt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clt.connect(("localhost",6000))

print(clt.recv(1024).decode())
