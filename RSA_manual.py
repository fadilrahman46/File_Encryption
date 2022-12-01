
"""
Created on Mon Nov 22 15:50:17 2021

@author: FADIL
"""
from decimal import Decimal

def gcd(k,totient):
    while totient!= 0:
        c = k % totient
        k = totient
        totient= c
        return k
#input variables
d=0
p = int(input('enter p : '))
q = int(input('enter q : '))
message = int(input('enter message : '))
#calculate n
n = p*q
#calculate totient
totient = (p-1)*(q-1)

#calculate K
for k in range(2,totient):
    if gcd(k,totient)== 1:
        break

for i in range(1,10):
    x = 1 + i*totient
    if x % k == 0:
        d = int(x/k)

    break

local_cipher = Decimal(0)
local_cipher =pow(message,k)
cipher_text = local_cipher % n

decrypt_t = Decimal(0)
decrypt_t= pow(cipher_text,d)
decrpyted_text = decrypt_t % n

print('n = '+str(n))
print('k = '+str(k))
print('totient = '+str(totient))
print('d = '+str(d))
print('cipher text = '+str(cipher_text))
print('decrypted text = '+str(decrpyted_text))