n = 119

print("Задача 1: разложение n=p*q перебором")
print("n =", n)

p = None
q = None

d = 2
while d <= n:
    if n % d == 0:
        p = d
        q = n // d
        break
    d += 1

print("p =", p)
print("q =", q)
print("Проверка:", p, "*", q, "=", p*q)
