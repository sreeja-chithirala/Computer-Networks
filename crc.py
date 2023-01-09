
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)
 
 
def mod2div(dividend, divisor):
 
    pick = len(divisor)
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
 
        if tmp[0] == '1':
 
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
 
        pick += 1
 
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword
 
def encodeData(data, key):
 
    l_key = len(key)
 
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
 
    codeword = data + remainder
    print("Remainder : ", remainder)
    print("Data received by the receiver (Data + Remainder) : ",
          codeword)

data = input("Enter the data to be sent: ")
key = input("Enter the key: ")
encodeData(data, key)

'''
output

Enter the data to be sent: 10110101
Enter the key: 1101
Remainder : 000
Data received by the receiver (Data + Remainder) : 10110101000

'''
