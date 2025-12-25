P = 7
Q = 3
d = 11
m = 2

def egcd(a, b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0

def modinv(a, mod):
    g, x, y = egcd(a, mod)
    if g != 1:
        return None
    return x % mod

print("Задача 4: RSA подпись")
n = P * Q
phi = (P - 1) * (Q - 1)
e = modinv(d, phi)  # открытый показатель для проверки

print("n =", n)
print("phi =", phi)
print("d (секретный) =", d)
print("e (открытый) =", e)
print()

h = m  # h(m)=m
s = pow(h, d, n)     # подпись
check = pow(s, e, n) # проверка

print("h(m) =", h)
print("Подпись s = h(m)^d mod n =", s)
print("Проверка: s^e mod n =", check)
print("Подлинность:", check == h)
