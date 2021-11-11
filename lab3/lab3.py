from Crypto.Util.number import *
from prime import * 
from lab1 import *
from hashlib import *
import sys
import math

def rsa_hash():
    message = md5(open('C:/Users/Tayler/Desktop/lab2/file/original.png', 'rb').read())
    message_int = int.from_bytes(message.digest(), byteorder='little')
    p = gen_p(1 << 128, (1 << 129))
    q = gen_p(1 << 128, (1 << 129))
    n = p * q
    fi = (p - 1) * (q - 1)
    d, c = gen_c_d(fi)
    assert n > message_int
    s = pow(message_int, c, n)
    e = pow(s, d, n)
    print(f'RSA H = {message_int}, e = {e}')

def el_gamal_hash():
    message = md5(open('C:/Users/Tayler/Desktop/lab2/file/original.png', 'rb').read())
    h = int.from_bytes(message.digest(), byteorder='little')
    p = getPrime(128)
    g = getPrime(128)
    x = rand_int(2, p - 1)
    y = pow(g, x, p)  
    k = mutually_prime(p - 1)
    r = pow(g, k, p)
    u = (h - x * r) % (p - 1)
    kk = inverse(k, p - 1)
    s = kk * u % (p - 1)
    yr = pow(y, r, p) * pow(r, s, p) % p
    gh = pow(g, h, p)
    print (f'Эль-Гамаль yr = {yr}, gh = {gh}')

def gost_hash():
    message = md5(open('C:/Users/Tayler/Desktop/lab2/file/original.png', 'rb').read())
    h = int.from_bytes(message.digest(), byteorder='little')
    q = getPrime(256)
    p = getPrime(1024)
    # while True: 
    #     b = rand_int(1 << 255, 1 << 256)
    #     if is_prime(p := b * q + 1):
    #         break
    b = rand_int(1 << 255, 1 << 256)
    while not is_prime(p := b * q + 1):
        b = rand_int(1 << 255, 1 << 256)
    while True:  
        g = rand_int(2, p - 1)
        if (a := pow(g, b, p)) > 1:
            break
    x = rand_int(1, q)
    y = modpow(a, x, p)
    while True:
        k = rand_int(1, q)
        if (r := pow(a, k, p) % q) == 0:
            continue
        if (s := (k * h % q + x * r % q) % q) != 0:
            break
    assert 0 < r < q
    assert 0 < s < q
    hh = inverse(h, q)
    u1 = s * hh % q
    u2 = -r * hh % q
    v = pow(a, u1, p) * pow(y, u2, p) % p % q
    #open('C:/Users/Tayler/Desktop/lab2/file/elgamal.txt', 'w').write(str(v)+str(r))
    print(f'ГОСТ v = {v},\n r = {r}')
    


# hash_object = md5(b'HelloWorld')
# print(hash_object.hexdigest())
# hash_object2 = sha1(b'HelloWorld')
# print(hash_object2.hexdigest())
# rsa_hash()
# el_gamal_hash()
gost_hash()