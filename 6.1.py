p = 29
Ca = 15
Cb = 25
m = 9

def egcd_with_steps(a, b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    steps = []
    while r1 != 0:
        q = r0 // r1
        steps.append((q, r0, r1, s0, s1, t0, t1))
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0, steps

def modinv_with_steps(a, mod):
    g, x, y, steps = egcd_with_steps(a, mod)
    print(f"Обобщ. Евклид для нахождения {a}^(-1) mod {mod}:")
    print("q | r0  r1 | s0  s1 | t0  t1")
    print("-" * 32)
    for q, r0, r1, s0, s1, t0, t1 in steps:
        print(f"{q:>1} | {r0:>3} {r1:>3} | {s0:>3} {s1:>3} | {t0:>3} {t1:>3}")
    if g != 1:
        return None
    return x % mod

print("Задача 1: Шифр Шамира")
print(f"p={p}, Ca={Ca}, Cb={Cb}, m={m}")
print("Нужно найти Da и Db такие, что Ca*Da≡1 (mod p-1) и Cb*Db≡1 (mod p-1)\n")

Da = modinv_with_steps(Ca, p - 1)
print("Da =", Da, "\n")

Db = modinv_with_steps(Cb, p - 1)
print("Db =", Db, "\n")

# Шаги протокола
x1 = pow(m, Ca, p)      # A
x2 = pow(x1, Cb, p)     # B
x3 = pow(x2, Da, p)     # A
x4 = pow(x3, Db, p)     # B

print("Шаги Шамира:")
print("x1 = m^Ca mod p =", x1)
print("x2 = x1^Cb mod p =", x2)
print("x3 = x2^Da mod p =", x3)
print("x4 = x3^Db mod p =", x4)

print("\nПроверка: x4 == m ?", x4 == m)
