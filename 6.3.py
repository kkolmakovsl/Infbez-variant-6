Pa, Qa, Da = 2, 11, 3
Pb, Qb, Db = 5, 7, 7
Mab = 17
Mba = 7

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

print("Задача 3: RSA (A<->B)")
Na = Pa * Qa
Nb = Pb * Qb
phi_a = (Pa - 1) * (Qa - 1)
phi_b = (Pb - 1) * (Qb - 1)

print("Параметры A:")
print("Na =", Na)
print("phi_a =", phi_a)
print("Da =", Da)

Ca = modinv(Da, phi_a)
print("Ca (обратный к Da mod phi_a) =", Ca)
print()

print("Параметры B:")
print("Nb =", Nb)
print("phi_b =", phi_b)
print("Db =", Db)

Cb = modinv(Db, phi_b)
print("Cb (обратный к Db mod phi_b) =", Cb)
print()

# A -> B
print("Передача A -> B")
c_ab = pow(Mab, Db, Nb)
m_ab = pow(c_ab, Cb, Nb)
print("Шифртекст c_ab = Mab^Db mod Nb =", c_ab)
print("Расшифр. m_ab = c_ab^Cb mod Nb =", m_ab)
print("Проверка m_ab == Mab ?", m_ab == Mab)
print()

# B -> A
print("Передача B -> A")
c_ba = pow(Mba, Da, Na)
m_ba = pow(c_ba, Ca, Na)
print("Шифртекст c_ba = Mba^Da mod Na =", c_ba)
print("Расшифр. m_ba = c_ba^Ca mod Na =", m_ba)
print("Проверка m_ba == Mba ?", m_ba == Mba)
