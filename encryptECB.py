from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encryptAndDecrypt(key, plaintext):
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    encryptedtext = b64encode(ct_bytes)
    print(f"The encrypted message is {encryptedtext.decode('utf-8')}")

encrypMessage = input("your message:")
encryptAndDecrypt('mypassword', encrypMessage)