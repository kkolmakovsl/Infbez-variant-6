a = 1050
b = 486

r0, r1 = a, b
s0, s1 = 1, 0
t0, t1 = 0, 1

print("Задача 4: ax + by = НОД(a,b) (обобщенный Евклид)")
print(f"a={a}, b={b}")
print("Шаги (q, r0, r1, s0, s1, t0, t1):")

while r1 != 0:
    q = r0 // r1
    print(f"q={q} | r0={r0}, r1={r1} | s0={s0}, s1={s1} | t0={t0}, t1={t1}")

    r0, r1 = r1, r0 - q * r1
    s0, s1 = s1, s0 - q * s1
    t0, t1 = t1, t0 - q * t1

# теперь r0 = gcd, s0 и t0 — коэффициенты
g = r0
x = s0
y = t0

print("\nНОД =", g)
print("x =", x)
print("y =", y)
print("Проверка:", a, "*", x, "+", b, "*", y, "=", a*x + b*y)
