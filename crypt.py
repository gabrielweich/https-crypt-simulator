"""
Autor: Gabriel Weich
Data: 26/11/2020
Linguagem: Python 3.7.3
"""

from Crypto import Random
from Crypto.Cipher import AES
import sys

class AESCipher:

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = bytes.fromhex(key)


    def decrypt(self, text, iv):
        iv = bytes.fromhex(iv)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(bytes.fromhex(text))).decode('utf-8')

    def encrypt(self, text):
        text = self._pad(text)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return (iv + cipher.encrypt(text.encode())).hex()
        
        
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


# key: dbe7faf1ab231dacd141938bae0143d8
# message: 5D127C2131EB42E7DF9C553C070B0D9B428027BFA53CF1D56ABC8C60F241455E1EC2BA506FB81410252953C600AE192F0EB04AAE4BFEBF123FA5EC962A625A46B0DC5AFB1933DCE5FDB4CEDB258237CFB2719315EE8152C300F9C4F85B2E2AA3


def main():
    password, message = sys.argv[1:]
    iv, msg = (message[:32], message[32:])
    aes = AESCipher(password)
    dec = aes.decrypt(msg, iv)
    print(dec)
    # Legal Gabriel. Agora inverte esta mensagem e me envia de volta cifrada

    dec = dec[::-1]

    print(aes.encrypt(dec))
    # b997bdbce6a39599c5db0bb0fce6dcee6cc9675a19554612de38f08a8c1dc3e9e2b3cb72a6e38087f33c4ad2138b7d65d609df71247c510f463581194138d6cb980872cde63031bdbd1978c79727e92b8d343a10674829337d8e67a1e5c2d5dd

if __name__ == "__main__":
    main()