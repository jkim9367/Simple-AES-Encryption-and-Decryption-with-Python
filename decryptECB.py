from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

def decrptECB(key, ciphertext):
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_ECB)
    secretmessage = b64decode(ciphertext)
    secretmessage = cipher.decrypt(secretmessage)
    secretmessage= unpad(secretmessage, AES.block_size)
    print(f"The decrypted message is: {secretmessage.decode('utf-8')} ")

decryptMessage = input("encrypted message:")
decrptECB('mypassword', decryptMessage)