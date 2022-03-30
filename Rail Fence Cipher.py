from itertools import chain

def encode(depth, str):
    arr = [0]*len(str)
    if depth==1:
        return str
    else:
        for i in range(len(str)):
            arr[i] = str[i]
    matrix = [[0 for i in range(len(str))] for j in range(depth)]
    result = []
    j=0
    i=0
  
    while(j<len(arr)):
        if depth<=2 and i>=depth:
            i=0
            matrix[i][j] = arr[j]
            i+=1
        elif i>=depth:
            i = depth-2
            while(i>0 and j<len(str)):
                matrix[i][j] = arr[j]
                
                i = i-1
                j+=1
            j-=1
        else:
            matrix[i][j] = arr[j]
            i+=1
        j+=1
    result = list(chain.from_iterable(matrix))
    result = [x for x in result if x!=0]

    ans = "" 
    for ele in result: 
        ans += ele  
    return ans 


def decode(depth, str):
    result = [0]*len(str)
    initalIndex = 0
    strIndex = 0
    for i in range(2*depth-2, -1, -2):
        if i == 0:
            inc = 2*depth-2
        else:
            inc = i
        j = initalIndex
        
        while j < len(str):
            if j != initalIndex:
                inc = 2*depth-2-inc
            if inc == 0:
                continue
                
            result[j] = (str[strIndex])
            strIndex +=1
            j = j+inc
        initalIndex+=1
    ans = ''
    for i in range(len(result)):
        ans += result[i]
    return ans

option = int(input("Select Option for rail fence cipher: \n1: Encode\n2: Decode\n"))

depth = int(input('Enter depth: '))
str = input('Enter text: ')

if option==1:
    print(encode(depth, str))
else:    
    print(decode(depth, str))
