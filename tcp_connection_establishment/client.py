import socket

clt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clt.connect(("localhost",12005))

msg=clt.recv(1024).decode()

clt.send("This is a msg from client".encode())

print(msg)
