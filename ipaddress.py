def basics(a,b,c,d):
    if 0<=a<=127:
        print(n+" belongs to classA.")
        print("The default subnet mask is 255.0.0.0")
        subnet="255.0.0.0"
        print("The number of hosts are: 2 ^ 24 - 2 = 16777214")
        print(f"The network id is: {a}.{0}.{0}.{0}")
        print(f"The broadcast id is: {a}.{255}.{255}.{255}")
    elif 128<=a<=191:
        print(n+" belongs to classB.")
        print("The default subnet mask is 255.255.0.0")
        subnet="255.255.0.0"
        print("The number of hosts are: 2 ^ 16 - 2 = 65534")
        print(f"The network id is: {a}.{b}.{0}.{0}")
        print(f"The broadcast id is: {a}.{b}.{255}.{255}")
    elif 192<=a<=223:
        print(n+" belongs to classC.")
        print("The default subnet mask is 255.255.255.0")
        subnet="255.255.255.0"
        print("The number of hosts are: 2 ^ 8 - 2 = 254")
        print(f"The network id is: {a}.{b}.{c}.{0}")
        print(f"The broadcast id is: {a}.{b}.{c}.{255}")
    elif 224<=a<=239:
        print(n+" belongs to classD.")
    elif 240<=a<=255:
        print(n+" belongs to classE.")


n=input("Enter the ip address: ")
a,b,c,d=map(int,n.split("."))
basics(a,b,c,d)
h=int(input("\nEnter the number of hosts: "))
if h>254:
    print("Invalid number of hosts")
else:
    for i in range(0,h):
        if 2**i-2>=h:
            break
    host_bits=i
    network_bits=32-host_bits

    subnet_mask=str(1)*network_bits+str(0)*host_bits
    a1=subnet_mask[:8]
    b1=subnet_mask[8:16]
    c1=subnet_mask[16:24]
    d1=subnet_mask[24:]
    print(f"The subnet mask is: {int(a1,2)}.{int(b1,2)}.{int(c1,2)}.{int(d1,2)}")
