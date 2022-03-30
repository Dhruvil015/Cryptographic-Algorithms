from collections import OrderedDict 

def getindexdefault(elem, arr):
    try:
        thing_index = arr.index(elem)
        return thing_index
    except ValueError:
        return -1

def encode(mode):
    mess = list(str(input("\nenter message : ")).upper().replace(" ", ""))
    key = str(input("enter key : ")).upper().replace(" ", "")
    message = []
    for i in range(0,len(mess),2):
        if i<len(mess)-2 and mess[i] == mess[i+1]:
            message.append(mess[i])
            message.append('X')
            message.append(mess[i+1])
        else:
            if i+1>=len(mess):
                message.append(mess[len(mess)-1])
                break
            else:
                message.append(mess[i])
                message.append(mess[i+1])

    if len(message)%2 != 0:
        message.append('X')

    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    alphabet = alphabet.upper()
    elements = key+alphabet
    elements = list("".join(OrderedDict.fromkeys(elements))) 
    matrix = [['' for i in range(6)] for j in range(6)]
    count=0
    for i in range(6):
        for j in range(6):
            matrix[i][j] = elements[count]
            count+=1
    result=[]
    for i in range(0,len(message),2):
        ele1 = []
        ele2 = []
        for j in range(6):
            firstele = getindexdefault(message[i], matrix[j])
            secondele = getindexdefault(message[i+1], matrix[j])
            if firstele != -1 and secondele != -1:
                ele1 = [j,firstele]
                ele2 = [j,secondele]
                break
            elif firstele != -1 and secondele == -1:
                ele1 = [j,firstele]
                continue
            elif firstele == -1 and secondele != -1:
                ele2 = [j,secondele]
                continue
            else:
                continue
        
        
        if mode == 'encoding':
            if ele1[0] == ele2[0] or ele1[1] == ele2[1]:
                for i in range(len(ele1)):
                    if ele1[i]>=5:
                        ele1[i] = -1
                    if ele2[i]>=5:
                        ele2[i] = -1

            if ele1[0] == ele2[0]:
                result.append(matrix[ele1[0]][ele1[1]+1])
                result.append(matrix[ele2[0]][ele2[1]+1])
                result.append(" ")
            elif ele1[1] == ele2[1]:
                result.append(matrix[ele1[0]+1][ele1[1]])
                result.append(matrix[ele2[0]+1][ele2[1]])
                result.append(" ")
            else :
                result.append(matrix[ele1[0]][ele2[1]])
                result.append(matrix[ele2[0]][ele1[1]])
                result.append(" ")
        
        elif mode == 'decoding':
            if ele1[0] == ele2[0]:
                if ele1[1]==0:
                    ele1[1] = 6
                if ele2[1]==0:
                    ele2[1] = 6
            elif ele1[1] == ele2[1]:
                if ele1[0]==0:
                    ele1[0] = 6
                if ele2[0]==0:
                    ele2[0] = 6

            if ele1[0] == ele2[0]:
                result.append(matrix[ele1[0]][ele1[1]-1])
                result.append(matrix[ele2[0]][ele2[1]-1])
                result.append(" ")
            elif ele1[1] == ele2[1]:
                result.append(matrix[ele1[0]-1][ele1[1]])
                result.append(matrix[ele2[0]-1][ele2[1]])
                result.append(" ")
            else :
                result.append(matrix[ele1[0]][ele2[1]])
                result.append(matrix[ele2[0]][ele1[1]])
                result.append(" ")

    return "".join(result)

def decode(mode):
    return encode(mode)

option = int(input(" \n1: Encode\n2: Decode\n Select Option for 6*6 Playfair Cipher: "))

if option == 1:
    print("\nresult = ",encode('encoding'),"\n")
elif option == 2:
    print("\nresult = ",decode('decoding'),"\n")