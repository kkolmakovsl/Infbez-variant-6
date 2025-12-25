c = 18
m = 19

print("Задача 3: обратный элемент перебором")
print("c =", c, "m =", m)

inv = None
x = 1
while x < m:
    if (c * x) % m == 1:
        inv = x
        break
    x += 1

print("inv =", inv)
print("Проверка:", (c * inv) % m)
