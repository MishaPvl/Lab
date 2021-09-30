from random import *
from math import ceil, sqrt


def modpow(base, exponent, mod):
    #base %= mod
    if exponent == 0:
        pw = 1
    elif exponent % 2 == 0:
        pw = modpow(base * base, exponent // 2, mod) % mod
    else:
        pw = (base * modpow(base, exponent - 1, mod)) % mod
    return pw

# def modpw(base, exp, mod):
#     r = 1
#     while(exp):
#         if exp & 0x01:
#             r = (r * base) % mod
#         base = (base * base) % mod
#         exp >>= 1
#     return r
def mod_pow(base, exp, mod):
    if exp == 0: return 1
    if exp & 1 == 0:
        r = mod_pow(base, exp // 2, mod)
        return (r * r) % mod
    else: return (base % mod * mod_pow(base, exp - 1, mod)) % mod

# Обобщенный алгоритм Евклида
# def gcd(a, b):
#     if a < b:
#         a, b = b, a
#     U = [a, 1, 0]
#     V = [b, 0, 1]
#     q = U[0] // V[0]
#     T = [U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2]]
#     while T[0] != 0:
#         q = U[0] // V[0]
#         #T = [U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2]]
#         T[0] = (U[0] % V[0])
#         T[1] = (U[1] - q * V[1])
#         T[2] = (U[2] - q * V[2])
#         U = V
#         V = T
#     print(f'x = {U[1]}, y = {V[1]}, gcd = {U[0]}, {a}, {b}')
#     print(a * U[1] + b * V[1])
#     return U

def gcd (a, b):
    if b == 0:
        x = 1
        y = 0
        return a, x, y
    d, x1, y1 = gcd(b, a % b)
    x = y1
    y = x1 - (a / b) * y1
    return d , x, y

def extgcd(a: int, b: int):
    if a <= 0 or b <= 0:
        raise ValueError("Числа могут быть только натуральными")
    # if a < b:
    #     a, b = b, a  # Ломает алгоритм
    u1, u2, u3 = a, 1, 0
    v1, v2, v3 = b, 0, 1
    while v1:
        q = u1 // v1
        t1, t2, t3 = u1 % v1, u2 - q * v2, u3 - q * v3
        u1, u2, u3 = v1, v2, v3
        v1, v2, v3 = t1, t2, t3
    return u1, u2, u3

def dh_system(xa, xb, p, g):
    q = (p - 1)/2
    print(f'q = {q}')
    Xa, Xb = xa, xb
    if modpow(g, q, p) != 1:
        Ya = modpow(g, Xa, p)
        Yb = modpow(g, Xb, p)
        Zab = modpow(Yb, Xa, p)
        Zba = modpow(Ya, Xb, p)
        return Ya, Yb, Zab, Zba
    else:
        print('Failed')

def bsgs(g, y, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime
    print(N)
    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(a, i, p): i for i in range(N)}
    print(tbl)
    # Precompute via Fermat's Little Theorem
    c = pow(a, N * (p - 2), p)
    print(c)
    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        k = (y * pow(c, j, p)) % p
        if k in tbl:
            return j * N + tbl[k]

    # Solution not found
    return None

def shanks(y: int, a: int, mod: int):
    """Вычисляет x для выражения y = a ** x % mod"""
    if y >= mod:
        y, mod = mod, y
    m = k = ceil(sqrt(mod))
    seq1 = {pow(a, j, mod) * y % mod: j for j in range(m)}
    seq2 = (pow(a, i * m, mod) for i in range(1, k + 1))
    for i, vel in enumerate(seq2, 1):
        if (j := seq1.get(vel)) is not None:
            return i * m - j
    return None

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def rand_prime(a, b):
    p = randint(a, b)
    if IsPrime(p):
        return p
    else:
        return rand_prime(a, b)


def rand_int(x, y):
    p = randint(x, y)
    return p


a = rand_int(0, 2**10)
b = rand_int(0, 2**10)
c = rand_int(0, 2**10)
xa = rand_prime(1, 2**10)
xb = rand_prime(1, 2**10)
p = rand_prime(1, 2**10)
g = rand_prime(1, 2**10)

#print(bsgs(5, 2, 23))
#print(shanks(2, 5, 23))
#print(shanks(xb, p, g))
#print(f'Xa = {xa}, Xb = {xb}, p = {p}, g = {g}')
#print(f'Первое число = {a}, Второе число = {b}, Третье число = {c}')
print(gcd(15, 4))
print(extgcd(15, 4))
#print(dh_system(xa, xb, p, g))
#print(modpow(9, 21, 69))

