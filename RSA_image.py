"""
Created on Fri Dec  3 09:58:26 2021

@author: FADIL
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64
def encrypt_blob(blob, public_key):
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    blob = zlib.compress(blob)
    chunk_size = 50000
    offset = 0
    end_loop = False
    encrypted =  ""
    while not end_loop:    
        chunk = blob[offset:offset + chunk_size]
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += bytes(" " * (chunk_size - len(chunk)),'utf-8')
        encrypted += str(rsa_key.encrypt(chunk))
        offset += chunk_size
    #print(type(encrypted))
    return base64.b64encode(encrypted.encode('ascii'))

fd = open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/pkey.txt", "rb")
public_key = fd.read()
fd.close()

fd = open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/img2.jpg", "rb")
unencrypted_blob = fd.read()
fd.close()

encrypted_blob = encrypt_blob(unencrypted_blob, public_key)
fd = open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/encrypted_img.jpg", "wb")
fd.write(encrypted_blob)
fd.close()