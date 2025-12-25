x = 179424
n = x
d = 2

factors = []  # (prime, power)

print("Задача 2: разложение на простые множители")
print("x =", x)
print("Делим по очереди:")

while d * d <= n:
    if n % d == 0:
        cnt = 0
        while n % d == 0:
            n //= d
            cnt += 1
            print(f"делим на {d} -> осталось {n}")
        factors.append((d, cnt))
    d += 1 if d == 2 else 2

if n > 1:
    factors.append((n, 1))

print("\nРазложение:")
out = []
for p, k in factors:
    if k == 1:
        out.append(str(p))
    else:
        out.append(f"{p}^{k}")
print(" * ".join(out))
