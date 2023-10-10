import math
import random


def checkPrime(value):
    if value == 0 or value == 1:
        return False
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True

def nextPrime(value):
    while True:
        value += 1
        if checkPrime(value):
            return value

def getPrime():
    prime = random.randint(0, 30000)
    if checkPrime(prime):
        return prime
    else:
        return nextPrime(prime)

def gcd(a, b):
    if a != 0:
        return gcd(b % a, a)
    return b

def getN(m):
    n = random.randint(0, m)
    while not (checkPrime(n) and gcd(n, m) == 1):
        n += 1
    return n


def nInverse(n, m):
    i = m
    v = 0
    d = 1
    while n > 0:
        t = i // n
        x = n
        n = i % x
        i = x
        x = d
        d = v - t * x
        v = x
    v %= m
    if v < 0:
        v = (v + m) % m
    return v