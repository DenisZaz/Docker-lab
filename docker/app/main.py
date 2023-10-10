
import random
import math
import os
from primalOperations import nextPrime, getN, nInverse
from stringOperations import charToBinary, binaryToChar

m = 0
n = 0


def superIncrSeq():
    seqSum = 0
    seq = []
    for i in range(8):
        seq.append(seqSum + random.randint(10, 20))
        seqSum += seq[i]
    
    print("Закрытый ключ: ", end="")
    for i in range(8):
        print(seq[i], end=" ")
    
    return seq

def getOpenKey(closedKey):
    openKey = []
    global m, n
    for i in range(8):
        m += closedKey[i]
    m = nextPrime(m)
    n = getN(m)
    
    for i in range(8):
        openKey.append((closedKey[i] * n) % m)
    
    print("\nm: ", m, "\tn: ", n)
    print("\nОткрытый ключ: ", end="")
    for i in range(8):
        print(openKey[i], end=" ")
    print("\n\n")
    
    return openKey

def encrypt(plaintext, openKey):
    cypher = []
    print("Шифр:   ", end="")
    for i in range(len(plaintext)):
        bin = charToBinary(plaintext[i])
        print(bin, "  ", end="")
        sum = 0
        for j in range(8):
            if bin[j] == '1':
                sum += openKey[j]
        cypher.append(sum)
        print(sum, " ", end="")
    return cypher



def decrypt(cypher, nInverse, m, closedKey):
    text = ""
    result = ""
 #   cypher.sort(reverse = True)k
    print(" \neasy: ", end="")
    for i in range(len(cypher)):
        symbolCode = [0,0,0,0,0,0,0,0]
        num = (cypher[i] * nInverse) % m
        print(num, "  ", end="")
        while num > 0:
            ind = 7
            for j in range(8):
                if closedKey[j] > num:
                    ind = j - 1
                    break
            symbolCode[ind] = 1;
        #    print(symbolCode)
            num -= closedKey[ind]
        text += binaryToChar(symbolCode)
    return text

closeKey = superIncrSeq()
openKey = getOpenKey(closeKey)

plaintext =  os.getenv("text")

encr = encrypt(plaintext, openKey)

nInv = nInverse(n, m)
print("\n\n nInverse : ", nInv)

text = decrypt(encr, nInv, m, closeKey)
print("\n\nРасшифрованный текст: ", text)