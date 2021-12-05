# Note, this script is not fully coded by me
# I just fixed it

def Encryption(message):
    try:
        key = 25
        encrypted_var=""
        if len(message) > 20:
            return "Message have to be smaller then 15 letters"
        else:
            for i in message:
                if(ord(i))>=65 and (ord(i)<=90):
                    temp=(ord(i)+key)
                    if temp>90:
                        temp=temp%90+64
                    encrypted_var=encrypted_var+chr(temp)
                elif(ord(i))>=97 and (ord(i)<=122):
                    temp=(ord(i)+key)
                    if temp>122:
                        temp=temp%122+96
                    encrypted_var=encrypted_var+chr(temp)
                else:
                    encrypted_var=encrypted_var+chr(ord(i)+key)
            return encrypted_var
    except:
        return "Error.."
def Decryption(message):
    try:
        if len(message) > 20:
            return "Message have to be smaller then 15 letters"
        else:
            key = 25
            decrypted_var=""
            for i in message:
                if((ord(i))>=65) and (ord(i))<=90:
                    decrypted_var=decrypted_var+chr((ord(i) - key-65) % 26 + 65)
                elif((ord(i))>=97) and (ord(i))<=122:
                    decrypted_var=decrypted_var+chr((ord(i) - key - 97) % 26 + 97)
                else:
                    decrypted_var=decrypted_var+chr(ord(i)-key)
            return decrypted_var
    except:
        return "Error.."