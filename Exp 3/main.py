from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

plaintText = b"This is a top secret."
cipherText = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"

myFile = open('words.txt', 'r')
lines = myFile.readlines()
words = [str.strip(line) for line in lines]
arr = []

for word in words:
    if len(word)<16:
        word=word.lower()
        key=word.encode()+b' '*(16-len(word))
        getCipher=AES.new(key, AES.MODE_CBC, iv=bytes.fromhex('0'*32))
        ciphertext=getCipher.encrypt(pad(plaintText, AES.block_size))
        match="Not Matched"
        if bytes.hex(ciphertext)==cipherText:
            match="Matched"
            arr.append(word)
        print(word,match)
print("\n\nThe final key is :",arr)
