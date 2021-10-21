from lab1 import *
import sys
import itertools
import operator

def final_message(bytes, file):
    for byte in bytes:
        file.write(byte.to_bytes(1, sys.byteorder))
def el_gamal():
    p, g = rand_prime(1, 10**9), rand_prime(1, 10**9)
    m = open('C:/Users/Tayler/Desktop/lab2/file/original.png', 'rb').read()
    ca, cb = rand_int(1, p - 1), rand_int(1, p - 1)
    da = modpow(g, ca, p)
    db = modpow(g, cb, p)
    k = rand_int(1, p - 2)
    r = modpow(g, k, p)
    encrypted = [byte * modpow(db, k, p) % p for byte in m]
    open('C:/Users/Tayler/Desktop/lab2/file/elgamal_encrypted.txt', 'w').write(str(encrypted))
    decrypted = [byte * pow(r, p - 1 - cb, p) % p for byte in encrypted]
    open('C:/Users/Tayler/Desktop/lab2/file/el.png', 'wb').write(bytes(decrypted))
    #final_message(decrypted, open('C:/Users/Tayler/Desktop/lab2/file/dec_original.png', 'wb'))

def rsa():
    pb, qb = rand_prime(1, 10**9), rand_prime(1, 10**9)
    nb = pb * qb
    fi = (pb - 1) * (qb - 1)
    db, cb = gen_c_d(fi)
    print(db, cb)
    m = open('C:/Users/Tayler/Desktop/lab2/file/original.png', 'rb').read()
    encrypted = [pow(byte, db, nb) for byte in m]
    open('C:/Users/Tayler/Desktop/lab2/file/rsa_enc.txt', 'w').write(str(encrypted))
    decrypted = [pow(byte, cb, nb) for byte in encrypted]
    open('C:/Users/Tayler/Desktop/lab2/file/rsa_dec.png', 'wb').write(bytes(decrypted))

def encrypt_shamir(data, power, mod):
    return [pow(byte, power, mod) for byte in data]

def shamir():
    p = rand_prime(1, 10**9)
    ca, da = gen_c_d(p - 1)
    cb, db = gen_c_d(p - 1)
    m = open('C:/Users/Tayler/Desktop/lab2/file/original.png', 'rb').read()
    x1 = encrypt_shamir(m, ca, p)
    x2 = encrypt_shamir(x1, cb, p)
    open('C:/Users/Tayler/Desktop/lab2/file/shamir_enc.txt', 'w').write(str(x2))
    x3 = encrypt_shamir(x2, da, p)
    x4 = encrypt_shamir(x3, db, p) 
    open('C:/Users/Tayler/Desktop/lab2/file/shamir_dec.png', 'wb').write(bytes(x4))

def vernam():
    m = open('C:/Users/Tayler/Desktop/lab2/file/original.png', 'rb').read()
    key = [rand_int(1, 256) for _ in range(len(m))]
    encrypted = list(itertools.starmap(operator.xor, zip(m, key)))
    open('C:/Users/Tayler/Desktop/lab2/file/vernam_dnc.txt', 'w').write(str(encrypted))
    decrypted = list(itertools.starmap(operator.xor, zip(encrypted, key)))
    open('C:/Users/Tayler/Desktop/lab2/file/vernam.png', 'wb').write(bytes(decrypted))


#el_gamal()
#rsa()
#shamir()
vernam()