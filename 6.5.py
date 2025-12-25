p = 47
g = 39
x = 14
m = 33
k = 45

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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
    g0, x0, y0 = egcd(a, mod)
    if g0 != 1:
        return None
    return x0 % mod

print("Задача 5: Подпись Эль-Гамаля")
print(f"p={p}, g={g}, x={x}, m={m}, k={k}")

# Проверка условия для k
if gcd(k, p - 1) != 1:
    print("k не подходит: gcd(k, p-1) != 1")
else:
    y = pow(g, x, p)          # открытый ключ
    r = pow(g, k, p)
    k_inv = modinv(k, p - 1)
    s = (k_inv * (m - x * r)) % (p - 1)

    print("\nОткрытый ключ y = g^x mod p =", y)
    print("r = g^k mod p =", r)
    print("k_inv = k^(-1) mod (p-1) =", k_inv)
    print("s = k_inv*(m - x*r) mod (p-1) =", s)

    # Проверка подписи:
    left = pow(g, m, p)
    right = (pow(y, r, p) * pow(r, s, p)) % p

    print("\nПроверка подписи:")
    print("g^m mod p =", left)
    print("y^r * r^s mod p =", right)
    print("Подлинность:", left == right)
