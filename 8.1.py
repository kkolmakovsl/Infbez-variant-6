p = 23
a = 10
y = 13

print("Задача 1: дискретный логарифм перебором")
print(f"Ищем x: {a}^x ≡ {y} (mod {p})\n")

value = 1  # a^0 mod p
x = 0

while x <= p - 2:
    print(f"x={x:2d} : {a}^{x} mod {p} = {value}")
    if value == y:
        print("\nОтвет: x =", x)
        break
    x += 1
    value = (value * a) % p

if x > p - 2:
    print("\nРешение не найдено в диапазоне 0..p-2")
