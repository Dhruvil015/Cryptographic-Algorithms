import math
import numpy as np
def encode(keyMatrix, message, alphabet, keymatrixLen):
    inputMatrix, symbolMatrix, alphMatrix  = [],[],[]

    # making message matix and symbol matrix
    for i in range(len(message)):
        if message[i].isnumeric() or (message[i] == " ") or (ord(message[i])<65 and ord(message[i])>90):
            symbolMatrix.append(i)
        else:
            alphMatrix.append(alphabet.index(message[i]))
    
    if len(alphMatrix)%keymatrixLen != 0:
        alphMatrix.append(alphabet.index("Z"))

    # paring message matrix (alphMatrix) with pair of two.
    for i in range(0, len(alphMatrix),2):
        inputMatrix.append([alphMatrix[i], alphMatrix[i+1]])

    # Transpose the input matrix for multiplication.
    rez = [[inputMatrix[j][i] for j in range(len(inputMatrix))] for i in range(len(inputMatrix[0]))]

    # multiplication and modluo by 26.
    multiArray= [[0 for  i in range(len(rez[0]))]for j in range(keymatrixLen)]
    for i in range(len(keyMatrix)):
        for j in range(len(rez[0])):
            for k in range(len(rez)):
                multiArray[i][j] += keyMatrix[i][k]*rez[k][j]
            multiArray[i][j] = multiArray[i][j]%26
    
    # Transpose the multiplication matrix.
    fArray = []    
    for j in range(len(multiArray[0])):
        for i in range(len(multiArray)):
            fArray.append(alphabet[multiArray[i][j]])
    
    # making final cipher array.
    cipherArr = []
    if len(symbolMatrix) != 0:
        size = len(symbolMatrix)+len(fArray)
        i=0
        inc = 0
        incfArray = 0
        while(i<size):
            if i in symbolMatrix:
                cipherArr.append(message[symbolMatrix[inc]])
                inc+=1
                i+=1
            else :
                cipherArr.append(fArray[incfArray])
                incfArray+=1
                i+=1
    else:
        cipherArr = fArray

    return "".join(cipherArr)



def decode(keyMatrix, message, alphabet, keymatrixLen):
    detValue = int(abs(np.linalg.det(keyMatrix)))

    i=1
    invOfDetValue = 0
    while(i>0):
        if (detValue*i)%26 == 1:
            invOfDetValue = i
            break
        else :
            i+=1

    # calculating adjoint and for negative adding 26 and making inverse matrix
    matrix = np.linalg.inv(keyMatrix)*(-detValue)
    for i in range(keymatrixLen):
        for j in range(keymatrixLen):
            if matrix[i][j] >= 0:
                matrix[i][j] = round(matrix[i][j])
            else : 
                matrix[i][j] = round(matrix[i][j]) + 26
    
    matrix = matrix.astype(int)
    return encode(matrix, message, alphabet, keymatrixLen)
    
option = int(input(" \n1: Encode\n2: Decode\n Select Option for Hill Cipher: "))

key = input("\nEnter key : ").upper()
message = input("Enter message : ").upper()
alphabet = list("ZABCDEFGHIJKLMNOPQRSTUVWXY")
keymatrixLen = int(math.sqrt(len(key)))

c=0
keyMatrix = [["" for  i in range(keymatrixLen)]for j in range(keymatrixLen)]
for i in range(keymatrixLen):
    for j in range(keymatrixLen):
        keyMatrix[i][j] = alphabet.index(key[c])
        c+=1

if option == 1:
    print("\nresult = ",encode(keyMatrix, message, alphabet, keymatrixLen),"\n")
elif option == 2:
    print("\nresult = ",decode(keyMatrix, message, alphabet, keymatrixLen),"\n")