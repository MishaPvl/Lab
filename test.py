from random import *
from math import ceil, sqrt


def modpow(base: int, exponent: int, mod: int):
    base %= mod
    if exponent == 0:
        pw = 1
    elif exponent % 2 == 0:
        pw = modpow(base * base, exponent // 2, mod) % mod
    else:
        pw = (base * modpow(base, exponent - 1, mod)) % mod
    return pw

# def babystepgiantstep(a, y, p):
#   m = k = ceil(sqrt(p))    
#   hashtable = {(pow_mod(a, i, p)*y)%p: i for i in range(m+1)}
#   print(hashtable.keys())
#   print(hashtable.values())
#   for j in range(1, k+1):
#         k = pow_mod(a, j*m, p)
#         if k in hashtable:
#             print(j*m-hashtable[k])
#             return (j*m-hashtable[k])

# print(babystepgiantstep(5, 2, 23))

# def shanks(y: int, a: int, mod: int):
#     if y >= mod:
#         y, mod = mod, y
#     print(f'(y = {y}, a = {a}, mod = {mod}')
#     m = k = ceil(sqrt(mod))
#     seq1 = {modpow(a, j, mod) * y % mod: j for j in range(m)}
#     seq2 = (modpow(a, i * m, mod) for i in range(1, k + 1))
#     for i, vel in enumerate(seq2, 1):
#         if (j := seq1.get(vel)) is not None:
#             r = i * m - j
#             print('Проверка: ', modpow(a, r, mod))
#             return r
#     return None

def dh_system(xa, xb, p, g):
    q = (p - 1)//2
    print(f'q = {q}')
    Xa, Xb = xa, xb
    if not(1 < g < p-1):
        p,g = g,p
    if modpow(g, q, p) != 1:
        Ya = modpow(g, Xa, p)
        Yb = modpow(g, Xb, p)
        Zab = modpow(Yb, Xa, p)
        Zba = modpow(Ya, Xb, p)
        return Ya, Yb, Zab, Zba
    else:
        print('Сгенерируйте новое число')

    

def rand_prime(a, b):
    p = randint(a, b)
    if IsPrime(p):
        return p
    else:
        return rand_prime(a, b)

        
def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

xa = rand_prime(1, 10**9)
xb = rand_prime(1, 10**9)
p = rand_prime(1, 10**9)
g = rand_prime(1, 10**9)
print(dh_system(xa, xb, p, g))