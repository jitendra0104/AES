from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

import base64

KEY = b'8bytekey'

def des_encrypt(plain_text):
    cipher = DES.new(KEY, DES.MODE_CBC, iv=KEY)
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode(), DES.block_size))
    return base64.b64encode(encrypted_bytes).decode()

def des_decrypt(cipher_text):
    cipher = DES.new(KEY, DES.MODE_CBC, iv=KEY)
    decrypted_bytes = unpad(cipher.decrypt(base64.b64decode(cipher_text)), DES.block_size)
    return decrypted_bytes.decode() 