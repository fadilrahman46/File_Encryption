"""
Created on Fri Dec  3 10:36:49 2021

@author: FADIL
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import base64
  
  
with open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/image_asli.jpg", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())
    image_encode = str(converted_string)
#print(converted_string)
  
with open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/encode_image_asli2.txt", "w") as file:
    file.write(image_encode)
    
keyPair = RSA.generate(1024)
pubKey = keyPair.publickey()
privKeyPEM = keyPair.exportKey()
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(image_encode)
cipher_ascii = binascii.hexlify(encrypted)
cipherteks = cipher_ascii.decode()

write_image = open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/encode_image_asli_enc.png", 'wb')
write_image.write(cipherteks)
write_image.close()