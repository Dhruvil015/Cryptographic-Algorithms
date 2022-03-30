def encode(message, shift):
    result_message = ''
    for i in message:
        if i.isupper():
            charCode = 65+((ord(i)-65 + shift)%26)
            character = chr(charCode)
            result_message = result_message + character
        elif i.islower():
            charCode = 97+((ord(i)-97 + shift)%26)
            character = chr(charCode)
            result_message = result_message + character
        else:
            result_message = result_message + i
    
    return result_message

def decode(message, shift):
    return encode(message, -shift)

choice = input("encode / decode : ")
message = input("Enter message : ")
shift = int(input("Enter shift :"))

if(choice == 'encode'):
    print("encoded message ==> ", encode(message, shift))
else:
    print("decoded message ==> ", decode(message, shift))

    

