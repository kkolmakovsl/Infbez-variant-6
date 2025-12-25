a = 20
b = 12

print("Задача 2: НОД перебором")
print("a =", a, "b =", b)

g = 1
d = 1
while d <= a and d <= b:
    if a % d == 0 and b % d == 0:
        g = d
    d += 1

print("НОД =", g)
