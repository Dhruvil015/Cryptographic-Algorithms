import random

def calculate_Key(p,q):
    n = p*q
    piN = (p-1)*(q-1)
    e = 0
    while(1):
        rand = random.randint(1,piN)
        if gcd(rand, piN)==1:
            e = rand
            break
    d = 0
    while(1):
        if (e*d)%piN==1:
            break
        d+=1
    return [[e,n],[d,n]]

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def ASCII(text):
    arr = []
    for i in text:
        arr.append(ord(i))
    return arr

def encode(key,lst):
    cipherArr = []
    print(f"e = {key[0][0]}")
    for i in range(len(lst)):
        cipherArr.append((lst[i]**key[0][0])%key[0][1])
    return cipherArr

def decode(key, msg):
    arr = []
    for i in msg:
        arr.append((i**key[1][0])%key[1][1])
    for i in range(len(arr)):
        arr[i] = chr(arr[i])
    return ''.join(arr)


p1 = int(input("\nEnter first prime number = "))
p2 = int(input("Enter second prime number = "))
key = calculate_Key(p1, p2)
message = input("Enter text to Encode = ")
asciiCodeArr = ASCII(message)
encoded = encode(key, asciiCodeArr)
print("\nEncoded message: ",encoded)
print("Decoded message: ",decode(key, encoded))