import socket

f=open("server.txt","r")
data=f.read()
s=socket.socket()
server_address=('localhost',6000)
s.bind(server_address)
s.listen(5)
print("Waiting for connection")
clt,client_address=s.accept()
print("Connection establissed: ",client_address)
clt.send(data.encode())

clt.close()
