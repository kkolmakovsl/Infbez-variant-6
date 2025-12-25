p = 40

n = p
phi = p
d = 2

print("Задача 1: φ(p)")
print("p =", p)
print("Разложение p на простые множители и применение формулы φ:")

while d * d <= n:
    if n % d == 0:
        print(f"Найден простой делитель {d}")
        while n % d == 0:
            n //= d
        old_phi = phi
        phi = phi - phi // d
        print(f"phi = {old_phi} - {old_phi}//{d} = {phi}")
    d += 1 if d == 2 else 2  # после 2 идем только по нечетным

if n > 1:
    d = n
    print(f"Найден простой делитель {d}")
    old_phi = phi
    phi = phi - phi // d
    print(f"phi = {old_phi} - {old_phi}//{d} = {phi}")

print("Ответ: φ(40) =", phi)
