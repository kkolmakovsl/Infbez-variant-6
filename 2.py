# Дано
n = [173, 200, 12]     # открытый текст (8 бит)
k = [138, 12, 212]     # ключ (8 бит)

print("Vernam (XOR) cipher for 8-bit numbers\n")

c = []
for i, (ni, ki) in enumerate(zip(n, k), start=1):
    # проверка, что это 8-битные числа
    if not (0 <= ni <= 255 and 0 <= ki <= 255):
        raise ValueError("Все числа должны быть в диапазоне 0..255")

    ci = ni ^ ki
    c.append(ci)

    b_ni = format(ni, "08b")
    b_ki = format(ki, "08b")
    b_ci = format(ci, "08b")

    print(f"Пара {i}:")
    print(f"  n{i} = {ni:3d} -> {b_ni}")
    print(f"  k{i} = {ki:3d} -> {b_ki}")
    print(f"  c{i} = n{i} XOR k{i}")
    print(f"       {b_ni}")
    print(f"   XOR {b_ki}")
    print(f"   =   {b_ci} -> {ci}\n")

print("Итоговый шифртекст (десятичный):", c)
