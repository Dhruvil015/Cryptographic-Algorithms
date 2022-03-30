def encode(message, key):
    result = []
    for i in range(len(message)):
        if message[i].isalpha():
            x = (ord(message[i].upper()) + ord(key[i]))%26
            x += ord('A')
            if message[i].isupper() == True:
                result.append(chr(x))
            else:
                result.append(chr(x).lower())
        else:
            result.append(message[i])
    return ("" . join(result))

def decode(message, key):
    result = []
    for i in range(len(message)):
        if message[i].isalpha():
            x = (ord(message[i].upper())-ord(key[i])+26)%26
            x += ord('A')
            if message[i].isupper() == True:
                result.append(chr(x))
            else:
                result.append(chr(x).lower())
        else:
            result.append(message[i])
    return ("" . join(result))


option = int(input(" \n1: Encode\n2: Decode\n Select Option for Vigenère Cipher: "))
message = list(str(input("\nEnter the message : ")))
messageKey = str(input("Enter the key : "))

key = []
j=0
for i in range(len(message)):
    if len(key) == len(message):
        break
    elif message[i].isalpha():
        key.append(messageKey[j % len(messageKey)].upper())
        j+=1
    else:
        key.append(message[i])

key = ("" . join(key))

if option == 1:
    print("\nresult = ",encode(message, key),"\n")
elif option == 2:
    print("\nresult = ",decode(message, key),"\n")
