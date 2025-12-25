p = 167
a = 101
y = 2
m = 13
k = 13

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

print("Задача 2: BSGS")
print(f"Ищем x: {a}^x ≡ {y} (mod {p})")
print(f"m={m}, k={k}\n")

# 1) Baby steps: a^j mod p, j=0..m-1
baby = {}
print("Baby steps: a^j mod p")
val = 1
for j in range(m):
    if val not in baby:
        baby[val] = j
    print(f"j={j:2d}: a^{j} mod p = {val}")
    val = (val * a) % p

# 2) factor = a^{-m} mod p
a_m = pow(a, m, p)
inv_a_m = modinv(a_m, p)
print("\nВычислим factor = a^(-m) mod p")
print("a^m mod p =", a_m)
print("inv(a^m) mod p =", inv_a_m)
factor = inv_a_m

# 3) Giant steps: gamma_i = y * factor^i mod p, i=0..k-1
print("\nGiant steps: gamma = y * (a^(-m))^i mod p")
gamma = y

found = False
for i in range(k):
    print(f"i={i:2d}: gamma = {gamma}", end="")
    if gamma in baby:
        j = baby[gamma]
        x = i * m + j
        print(f"  -> найдено совпадение с baby: j={j}")
        print("\nОтвет: x =", x)
        found = True
        break
    else:
        print("  -> нет совпадения")
    gamma = (gamma * factor) % p

if not found:
    print("\nСовпадение не найдено при заданных m и k")
