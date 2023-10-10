def charToBinary(ch):
    bin = ""
    for i in range(7, -1, -1):
        bin += str((ord(ch) >> i) & 1)
    return bin

def binaryToChar(bin):
    ch = 0
    for i in range(8):
        ch += int(bin[i]) * pow(2, 7 - i)
    return chr(ch)