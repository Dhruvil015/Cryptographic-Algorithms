import math
def encode(message, mkey, row, col):     

    matrix = [['X' for i in range(col)] for j in range(row)]
    count=0
    for i in range(row):
        for j in range(col):
            if count >= len(message):
                break
            matrix[i][j] = message[count]
            count+=1

    arr=[]
    for ele in mkey:
        for i in range(row):
            arr.append(matrix[i][int(ele[1])])

    return ("".join(arr))


def decode(message, mkey, row, col):

    matrix = [['X' for i in range(col)] for j in range(row)]
    count=0
    for ele in mkey:
        for i in range(row):
            if count >= len(message):
                break
            matrix[i][int(ele[1])] = message[count]
            count+=1

    arr=[]
    for i in range(row):
        for j in range(col):
            arr.append(matrix[i][j])

    return ("".join(arr))



option = int(input(" \n1: Encode\n2: Decode\n Select Option row Transposition Cipher: "))
message = str(input("\nEnter the message : "))
mkey = list(map(list, input("Enter the key: ")))

for i in range(len(mkey)):
    mkey[i].append(i)
mkey.sort(key = lambda x:x[0])

row = math.ceil(len(message)/len(mkey))
col = len(mkey)

if option==1:
    print("\nresult = ",encode(message, mkey, row, col),"\n")
elif option==2:    
    print("\nresult = ",decode(message, mkey, row, col),"\n")
