a = 30691752
b = 30493400

A, B = a, b
print("Задача 1: НОД алгоритмом Евклида")
print(f"a={a}, b={b}")
print("Шаги (A = B*q + r):")

while B != 0:
    q = A // B
    r = A % B
    print(f"{A} = {B}*{q} + {r}")
    A, B = B, r

print("НОД =", A)
