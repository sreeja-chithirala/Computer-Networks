s=list(map(int,input("Enter the data to be transferred: ")))
r=0
while 2**r<len(s)+r+1:
    r+=1
s.reverse()
for i in range(r):
    s.insert((2**i)-1,"#")
i=0
while i!=r:
    tmp=[]
    t=2**i
    while(True):
        for k in range(t,t+(2**i)):
            if k>len(s):
                break
            if type(s[k-1])==int:
                tmp.append(s[k-1])
        t=t+2*(2**i)
        if t>len(s):
            break
    i+=1
    if tmp.count(1)%2==0:
        s[s.index("#")]=0
    else:
        s[s.index("#")]=1
s.reverse()
s=list(map(str,s))
print("The data received is: ",end=" ")
print("".join(s))


'''

output

Enter the data to be transferred: 1001101
The data received is: 10011100101

'''
