"""
Autor: Gabriel Weich
Data: 26/11/2020
Linguagem: Python 3.7.3
"""

import hashlib

# Formata texto de p e g
def format_lines(lines):
    return ''.join(lines).replace('\n', '').replace(' ', '')


# Lê o arquivo contento g
with open('g.txt') as f:
    g = int(format_lines(f.readlines()), 16) 


# Lê o arquivo contento p
with open('p.txt') as f:
    p = int(format_lines(f.readlines()), 16)


# Valor definido de a
a = 106353

# Calcula o valor de A (A = g^a mod p)
A = (g**a) % p
print("Valor de A (hexa): ", format(A, 'x'), '\n')

# Valor enviado (hex(A)): 9288d5fdc00fdd4376b3feff24705fcec290c1bc26d641cce76fbe587e3d66be7b71c3f3af35eab74418cce5aa94b25e0b580191e60a771257774e81031cc2322944afaa737f5f515a90a2abaab5f2164cf7fc69c94c1b9b7c635cf0b35f9e9afbfaacd5ae9da4af398bfafba023e23b7899134ad41b3c8812cd1fd8a1433905

# Valor recebido (hex(B)): 6B421D64ABFCB78338FCB4ECA296A63835FD84E9F9E50ECB611129BDD371DCEDBF114FBBE526268EBC04CD750431F4A88484DEB5AD523C8A1EF1A0D46C5D487742F25449242ABE3A9C24CD1E706A64C9790CB6EE10C36CB77D36F9AB15E98300660353159A079A397D25BABE4906EC10647402571AE03BF23AE114E79A31711D

B = int('6B421D64ABFCB78338FCB4ECA296A63835FD84E9F9E50ECB611129BDD371DCEDBF114FBBE526268EBC04CD750431F4A88484DEB5AD523C8A1EF1A0D46C5D487742F25449242ABE3A9C24CD1E706A64C9790CB6EE10C36CB77D36F9AB15E98300660353159A079A397D25BABE4906EC10647402571AE03BF23AE114E79A31711D', 16)


# Calcula o valor de V (V = B^a mod p)
V = (B ** a) % p
print("Valor de V: ", V, '\n')

# Transforma V em hexa
V_h = format(V, 'x')

# Transforma V de hexa para bytearray
V_b = bytearray.fromhex(V_h)

# Gera um hash de V_b usando sha-256 e usa os primeiros 128 bits como senha
S = hashlib.sha256(V_b) 
print('Senha: ', S.hexdigest()[:32])

# Valor da senha: 9eb06076d3fe4921de0d536efd2fa4c5