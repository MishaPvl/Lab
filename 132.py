# Write your code here :-)

from random import *
from math import ceil, sqrt


def modpow(base: int, exponent: int, mod: int):
    #base %= mod
    if exponent == 0:
        pw = 1
    elif exponent % 2 == 0:
        pw = modpow(base * base, exponent // 2, mod) % mod
    else:
        pw = (base * modpow(base, exponent - 1, mod)) % mod
    return pw

def mod_pow(base, exp, mod):
    if exp == 0: return 1
    if exp & 1 == 0:
        r = mod_pow(base, exp // 2, mod)
        return (r * r) % mod
    else: return (base % mod * mod_pow(base, exp - 1, mod)) % mod

# Обобщенный алгоритм Евклида
def gcd(a, b):
    if a < b:
        a, b = b, a
    U = [a, 1, 0]
    V = [b, 0, 1]
    while V[0] != 0:
        q = U[0] // V[0]
        T = [U[0] % V[0], U[1] - q * V[1], U[2] - q * V[2]]
        U = V
        V = T
    print(f'x = {U[1]}, y = {U[2]}, gcd = {U[0]}, a = {a}, b = {b}')
    print('a*x+b*y =', a * U[1] + b * U[2])
    return U


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

def shanks(y: int, a: int, mod: int):
    if y >= mod:
        y, mod = mod, y
    print(f'(y = {y}, a = {a}, mod = {mod}')
    m = k = ceil(sqrt(mod))
    seq1 = {modpow(a, j, mod) * y % mod: j for j in range(m)}
    seq2 = (modpow(a, i * m, mod) for i in range(1, k + 1))
    for i, vel in enumerate(seq2, 1):
        if (j := seq1.get(vel)) is not None:
            r = i * m - j
            print('Проверка: ', modpow(a, r, mod))
            return r
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


a = rand_int(0, 10**9)
b = rand_int(0, 10**9)
c = rand_int(0, 10**9)
xa = rand_prime(1, 10**9)
xb = rand_prime(1, 10**9)
p = rand_prime(1, 10**9)
g = rand_prime(1, 10**9)

print('Быстрое возведение в степень по модулю')
print(f'Первое число = {a}, Второе число = {b}, Третье число = {c}')
#print(modpow(a, b, c))
print('*'*50)
print('Обобщенный алгоритм Евклида')
print(gcd(a, b))
print('*'*50)
print('Д-Х')
print(f'Xa = {xa}, Xb = {xb}, p = {p}, g = {g}')
print(dh_system(xa, xb, p, g))
print('*'*50)
print('Шаг младенца, шаг великана')
print(shanks(a, b, p))

#print(bsgs(5, 2, 23))
#print(extgcd(15, 4))
#print(gcd(15, 4))

#print(modpow(9, 21, 69))