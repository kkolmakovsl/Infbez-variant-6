def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

pairs = [(52, 73), (39, 98), (82, 96)]

print("Задача 3: взаимно простые пары")
for idx, (x, y) in enumerate(pairs, start=1):
    g = gcd(x, y)
    if g == 1:
        print(f"Пара {idx}: ({x}, {y}) -> взаимно простые (НОД=1)")
    else:
        print(f"Пара {idx}: ({x}, {y}) -> НЕ взаимно простые (НОД={g})")
