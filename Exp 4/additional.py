
from Crypto.PublicKey import RSA

from Crypto.Util import asn1
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import PKCS1_OAEP
import sys

msg = b"hello..."

if (len(sys.argv)>1):

    msg=str(sys.argv[1])

key = RSA.generate(1024)

binPrivKey = key.exportKey('PEM')
binPubKey =	key.publickey().exportKey('PEM')

print()
print("====Private key===")

print(binPrivKey)
print()
print("====Public key===")

print(binPubKey)

privKeyObj = RSA.importKey(binPrivKey)

pubKeyObj =	RSA.importKey(binPubKey)

cipher = PKCS1_OAEP.new(pubKeyObj)
ciphertext = cipher.encrypt(msg)

print
print("====Ciphertext===")
print(b64encode(ciphertext))

cipher = PKCS1_OAEP.new(privKeyObj)
message = cipher.decrypt(ciphertext)

print()

print("====Decrypted===")
print("Message:",message)
