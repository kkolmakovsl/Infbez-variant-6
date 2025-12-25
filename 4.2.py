a = 4041
b = 6258

# НОД (Евклид)
A, B = a, b
while B != 0:
    A, B = B, A % B
g = A

lcm = (a // g) * b  # безопаснее, чем a*b//g

print("Задача 2: НОК(a,b)")
print(f"a={a}, b={b}")
print("НОД =", g)
print("НОК =", lcm)
