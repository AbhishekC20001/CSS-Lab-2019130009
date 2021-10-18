print('Crypto Method Menu')
print('1 Substitution')
print('2 ROT 13')
print('3 Transpose')
print('4 Double Transposition')
print('5 Vernam Cipher')
print('6 Diffie – Hellman')
print()

a =(int)(input('Enter the Crypto Method: '))
print()

def encrypt(b, key):
  matrix = createMatrix(len(key), b)
  sequence = getSequence(key)
  ans = ""
  for num in range(len(sequence)):
    pos = sequence.index(num+1)
    for row in range(len(matrix)):
      if len(matrix[row]) > pos:
        ans += matrix[row][pos]
  return ans

def createMatrix(width, b):
  r = 0
  c = 0
  matrix = [[]]
  for pos, ch in enumerate(b):
    matrix[r].append(ch)
    c += 1
    if c >= width:
      c = 0
      r += 1
      matrix.append([])

  return matrix

def getSequence(key):
  sequence = []
  for pos, ch in enumerate(key):
    previousLetters = key[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence

def decrypt(message, keyword):
  matrix = createDecrMatrix(getSequence(keyword), message)

  plaintext = ""
  for r in range(len(matrix)):
    for c in range (len(matrix[r])):
      plaintext += matrix[r][c]
  return plaintext


def createDecrMatrix(keywordSequence, message):
  width = len(keywordSequence)
  height = len(message) // width
  if height * width < len(message):
    height += 1

  matrix = createEmptyMatrix(width, height, len(message))

  pos = 0
  for num in range(len(keywordSequence)):
    column = keywordSequence.index(num+1)

    r = 0
    while (r < len(matrix)) and (len(matrix[r]) > column):
      matrix[r][column] = message[pos]
      r += 1
      pos += 1

  return matrix


def createEmptyMatrix(width, height, length):
  matrix = []
  totalAdded = 0
  for r in range(height):
    matrix.append([])
    for c in range(width):
      if totalAdded >= length:
        return matrix
      matrix[r].append('')
      totalAdded += 1
  return matrix


def encryptS(b,k):
    newS = ''
    for i in range(len(b)):
        val = ord(b[i])
        dup = k
        d = val + k
        if val >= 97 and val <= 122:
            if d > 122:
                k -= (122 - val)
                k = k % 26
                newS += chr(96 + k)
            else:
                newS += chr(d)
            k = dup
        elif val >= 65 and val <= 90:
            if d > 90:
                k -= (90 - val)
                k = k % 26
                newS += chr(64 + k)
            else:
                newS += chr(d)
            k = dup
        else:
            newS += chr(d)
    return newS

def decryptS(b,k):
    s = ''
    for i in range(len(b)):
        val = ord(b[i])
        dup = k
        d = val-k
        if val >= 97 and val <= 122:
            if d < 97:
                k += (122-val)
                k = k%26
                s += chr(122 - k)
            else:
                s += chr(d)
            k = dup
        elif val >= 65 and val <= 90:
            if d < 65:
                k += (90 - val)
                k = k%26
                s += chr(90 - k)
            else:
                s += chr(d)
            k = dup
        else:
            s += chr(d)
    return s

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encryptVernam(b,final_key):
    b_list = []
    k_list = []
    final_l = []
    for c in b:
        b_list.append(ord(c) - 65)
    for d in final_key:
        k_list.append(ord(d) - 65)
    for i in range(0, len_b):
        final_l.append((b_list[i] + k_list[i]) % 26)
    ans = ''
    for i in range(0, len_b):
        ans = ans + chr(final_l[i] + 65)
    return ans


def decryptVername(encrypted,key):
    orig_text = []
    for i in range(len(encrypted)):
        d = (ord(encrypted[i])-ord(key[i])+26)%26
        d += ord('A')
        orig_text.append(chr(d))
    return ("".join(orig_text))

if a==1:
    b = input('Enter message: ')
    k = int(input('Number of positions to be shifted: '))
    s = encryptS(b,k)
    print('Encrypted Message: ',s)
    print('Decrypted Message: ',decryptS(s,k))
elif a==2:
    b = input('Enter message: ')
    newS = ''
    s = encryptS(b, 13)
    print('Encrypted Message: ', s)
    print('Decrypted Message: ', decryptS(s, 13))


elif a==3:
    b = input('Enter message: ')
    key = input('Enter key: ')
    encypted = (encrypt(b,key))
    print('Encrypted Message: ',encypted)
    decrypted = decrypt(encypted,key)

    print('Decrypted Message: ',decrypted)
elif a==4:
    b = input('Enter message: ')
    key = input('Enter key: ')
    encrypted = encrypt(encrypt(b,key),key)
    print(encrypted)
    decrypted = decrypt(decrypt(encrypted,key),key)

    print(decrypted)
elif a==5:
    b = input('Enter message: ').replace(" ", "")
    b.upper()
    len_b = len(b)
    key = input('Enter key: ')
    key.upper()
    final_key = generateKey(b,key)
    encrypted = (encryptVernam(b,final_key))
    decrypted = decryptVername(encrypted,final_key)
    print(encrypted)
    print(decrypted)
elif a==6:
    #P = 23
    #G = 9
    P = int(input('Enter Prime Number P: '))
    G = int(input('Enter Prime Number G: '))
    #print('The Value of P is :%d'%(P))
    #print('The Value of G is :%d'%(G))

    a = int(input('Enter Private KeyA for Alice: '))
    x = int(pow(G,a,P))

    b = int(input('Enter Private KeyB for Bob: '))
    y = int(pow(G,b,P))

    ka = int(pow(y,a,P))

    kb = int(pow(x,b,P))

    print('Secret key for the Alice is : %d'%(ka))
    print('Secret Key for the Bob is : %d'%(kb))
