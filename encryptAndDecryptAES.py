from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

def encryptAndDecrypt(key, plaintext):
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    encryptedtext = b64encode(ct_bytes)
    print(f"The encrypted message is {encryptedtext.decode('utf-8')}")

    secretmessage = b64decode(encryptedtext.decode('utf-8'))
    secretmessage = cipher.decrypt(secretmessage)
    secretmessage= unpad(secretmessage, AES.block_size)
    print(f"The decrypted message is: {secretmessage.decode('utf-8')} ")

Message = input("Enter message:")
encryptAndDecrypt('mypassword', Message)