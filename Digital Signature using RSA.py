import math
import random
def gcd(x,y):
    if not(y):
        return x
    else:
        return gcd(y, x%y)

def genrateKeys(p,q):
    n = p*q
    et = (p - 1) * (q - 1)
    d=0
    while(1):
        e = 313
        if(gcd(e,et) == 1):
            break
    
    while(1):
        if((e * d) % et == 1):
            break
        d+=1
    
    return [[e,n], [d,n]]

def cipherFunction(arr, key):
    for i in range(len(arr)):
        arr[i] = chr(int((arr[i]**key[0])%key[1]))
    return arr

def encodeText(str, key):
    arr = []
    for i in str:
        arr.append(ord(i))     
    return [str, "".join(cipherFunction(arr,key))]

def decodeText(sign, key):
    arr = []
    for i in sign[1]:
        arr.append(ord(i)) 
    return [sign[0], "".join(cipherFunction(arr, key)) == sign[0]]

str = "Dhruvil lathiya"
[enkey,dekey] =  genrateKeys(823, 953)

encodeStr = encodeText(str, enkey)
print("signature : ", encodeStr[1])
print("message : ", encodeStr[0])

decodeStr = decodeText(encodeStr, dekey)
print("verify signature : " , decodeStr[1])
print("received message: ", decodeStr[0]  if decodeStr[1] else "")