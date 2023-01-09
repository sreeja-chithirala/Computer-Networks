import socket

s=socket.socket()
#server_address=('10.1.34.80',12001)
s.bind(('localhost',12005))
s.listen(20)
print("Waiting for connection")

clt,client_address=s.accept()

print("Connecttion established",client_address)
clt.send("This is a msg from server".encode())

msg=clt.recv(1024).decode()
print(msg)
