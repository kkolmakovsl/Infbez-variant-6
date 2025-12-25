c = 5
m = 138

r0, r1 = c, m
s0, s1 = 1, 0
t0, t1 = 0, 1

print("Задача 5: обратный элемент c^-1 mod m (обобщенный Евклид)")
print(f"c={c}, m={m}")
print("Шаги (q, r0, r1, s0, s1, t0, t1):")

while r1 != 0:
    q = r0 // r1
    print(f"q={q} | r0={r0}, r1={r1} | s0={s0}, s1={s1} | t0={t0}, t1={t1}")

    r0, r1 = r1, r0 - q * r1
    s0, s1 = s1, s0 - q * s1
    t0, t1 = t1, t0 - q * t1

g = r0
x = s0  # коэффициент при c в равенстве c*x + m*y = gcd

if g != 1:
    print("\nОбратного элемента нет, т.к. НОД(c,m) != 1")
else:
    inv = x % m
    print("\nНОД(c,m) =", g)
    print("Инверсия:", inv)
    print("Проверка:", (c * inv) % m)
