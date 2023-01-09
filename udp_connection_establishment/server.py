import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('localhost',15000))

print("Waiting for connection")


msg,address=s.recvfrom(1024)
print("Connected to "+str(address))
print(msg)
s.sendto("This is UDP server".encode(),address)
