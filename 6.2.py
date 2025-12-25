p = 47
g = 11
Ca = 2
Cb = 24
Mab = 26
Mba = 32
Kab = 36
Kba = 30

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

print("Задача 2: Эль-Гамаль (шифрование A->B и B->A)")
print(f"p={p}, g={g}, Ca={Ca}, Cb={Cb}")
print(f"Mab={Mab}, Mba={Mba}, Kab={Kab}, Kba={Kba}\n")

# Публичные ключи
Ya = pow(g, Ca, p)
Yb = pow(g, Cb, p)
print("Публичные ключи:")
print("Ya = g^Ca mod p =", Ya)
print("Yb = g^Cb mod p =", Yb)
print()

# -------- A -> B --------
print("Передача A -> B")
r_ab = pow(g, Kab, p)
s_ab = pow(Yb, Kab, p)
e_ab = (Mab * s_ab) % p

print("r_ab = g^Kab mod p =", r_ab)
print("s_ab = Yb^Kab mod p =", s_ab)
print("e_ab = Mab * s_ab mod p =", e_ab)

# Расшифрование у B
s_ab_recv = pow(r_ab, Cb, p)
inv_s = modinv(s_ab_recv, p)
Mab_recv = (e_ab * inv_s) % p

print("s_ab_recv = r_ab^Cb mod p =", s_ab_recv)
print("inv(s_ab_recv) mod p =", inv_s)
print("Mab_recv = e_ab * inv(s_ab_recv) mod p =", Mab_recv)
print("Проверка Mab_recv == Mab ?", Mab_recv == Mab)
print()

# -------- B -> A --------
print("Передача B -> A")
r_ba = pow(g, Kba, p)
s_ba = pow(Ya, Kba, p)
e_ba = (Mba * s_ba) % p

print("r_ba = g^Kba mod p =", r_ba)
print("s_ba = Ya^Kba mod p =", s_ba)
print("e_ba = Mba * s_ba mod p =", e_ba)

# Расшифрование у A
s_ba_recv = pow(r_ba, Ca, p)
inv_s2 = modinv(s_ba_recv, p)
Mba_recv = (e_ba * inv_s2) % p

print("s_ba_recv = r_ba^Ca mod p =", s_ba_recv)
print("inv(s_ba_recv) mod p =", inv_s2)
print("Mba_recv = e_ba * inv(s_ba_recv) mod p =", Mba_recv)
print("Проверка Mba_recv == Mba ?", Mba_recv == Mba)
