# Практическое задание 2.2 — Эллиптические кривые
# Без import. Консольное меню.

# ------------------------
# Базовые функции
# ------------------------

def is_prime(p):
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    d = 3
    while d * d <= p:
        if p % d == 0:
            return False
        d += 2
    return True

def egcd(a, b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0  # gcd, x, y

def modinv(a, mod):
    a %= mod
    g, x, y = egcd(a, mod)
    if g != 1:
        return None
    return x % mod

# ------------------------
# 1) Групповой закон (умножение) в Fp*
# ------------------------

def mult_table_fp_star(p):
    if not is_prime(p):
        print("Ошибка: p должно быть простым.")
        return

    elems = list(range(1, p))  # Fp* = {1..p-1}
    w = len(str(p - 1)) + 1

    print("\nГрупповой закон для остатков mod p (операция умножения), p =", p)
    print("Элементы группы: 1..", p - 1)
    print()

    # header
    print("".rjust(w), end="")
    for x in elems:
        print(str(x).rjust(w), end="")
    print()

    # rows
    for a in elems:
        print(str(a).rjust(w), end="")
        for b in elems:
            print(str((a * b) % p).rjust(w), end="")
        print()

# ------------------------
# 2) Порядок элемента в Fp* + генераторы
# ------------------------

def order_in_fp_star(a, p):
    # порядок a в мультипликативной группе mod p
    # p простое, a in [1..p-1]
    val = 1
    k = 0
    while True:
        k += 1
        val = (val * a) % p
        if val == 1:
            return k

def orders_table_fp_star(p):
    if not is_prime(p):
        print("Ошибка: p должно быть простым.")
        return

    print("\nПорядки элементов в группе Fp* (mod p), p =", p)
    print("Генератор: порядок = p-1 =", p - 1)
    print()

    w1 = len(str(p - 1)) + 1
    print("a".rjust(w1), "ord(a)".rjust(w1), "генератор")
    print("-" * (w1 * 2 + 12))

    for a in range(1, p):
        ord_a = order_in_fp_star(a, p)
        gen = "*" if ord_a == p - 1 else ""
        print(str(a).rjust(w1), str(ord_a).rjust(w1), "   ", gen)

# ------------------------
# Эллиптическая кривая: y^2 = x^3 + A*x + B (mod p)
# ------------------------

O = None  # точка бесконечности будем обозначать как None

def ec_is_singular(p, A, B):
    # условие несингулярности: 4A^3 + 27B^2 != 0 (mod p)
    return (4 * (A * A % p) * A + 27 * (B * B % p)) % p == 0

def ec_on_curve(P, p, A, B):
    if P is O:
        return True
    x, y = P
    return (y * y - (x * x * x + A * x + B)) % p == 0

def ec_add(P, Q, p, A):
    # Сложение точек на ЭК
    if P is O:
        return Q
    if Q is O:
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P) = O
    if x1 == x2 and (y1 + y2) % p == 0:
        return O

    if P != Q:
        num = (y2 - y1) % p
        den = (x2 - x1) % p
        inv_den = modinv(den, p)
        if inv_den is None:
            return O
        lam = (num * inv_den) % p
    else:
        # удвоение
        if y1 % p == 0:
            return O
        num = (3 * x1 * x1 + A) % p
        den = (2 * y1) % p
        inv_den = modinv(den, p)
        if inv_den is None:
            return O
        lam = (num * inv_den) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_points(p, A, B):
    # все точки на ЭК над Fp, включая O
    pts = [O]
    for x in range(p):
        rhs = (x * x * x + A * x + B) % p
        for y in range(p):
            if (y * y) % p == rhs:
                pts.append((x, y))
    return pts

def pt_str(P):
    if P is O:
        return "O"
    return f"({P[0]},{P[1]})"

# ------------------------
# 3) M-кратная композиция точки: M*P (double-and-add) + шаги
# ------------------------

def ec_mul_verbose(M, P, p, A):
    print("\nM-кратная композиция (скалярное умножение):")
    print("M =", M, ", P =", pt_str(P))
    print("Бинарно: M =", bin(M))
    print()

    R = O
    Q = P
    step = 0

    while M > 0:
        step += 1
        bit = M & 1
        print(f"Шаг {step}: bit={bit}, R={pt_str(R)}, Q={pt_str(Q)}")
        if bit == 1:
            before = R
            R = ec_add(R, Q, p, A)
            print("  R = R + Q:", pt_str(before), "+", pt_str(Q), "=", pt_str(R))
        beforeQ = Q
        Q = ec_add(Q, Q, p, A)
        print("  Q = 2Q:", pt_str(beforeQ), "->", pt_str(Q))
        M >>= 1
        print()

    print("Результат: R =", pt_str(R))
    return R

# ------------------------
# 4) Таблица группового закона для точек ЭК
# ------------------------

def ec_add_table(p, A, B):
    if not is_prime(p):
        print("Ошибка: p должно быть простым.")
        return
    if ec_is_singular(p, A, B):
        print("Ошибка: кривая сингулярна (4A^3 + 27B^2 ≡ 0 mod p).")
        return

    pts = ec_points(p, A, B)
    labels = [pt_str(P) for P in pts]

    # ширина по самому длинному ярлыку
    w = max(len(s) for s in labels) + 1

    print("\nГрупповой закон для точек ЭК: P + Q")
    print(f"p={p}, A={A}, B={B}")
    print("Число точек |E(Fp)| =", len(pts))
    print()

    # header
    print("".rjust(w), end="")
    for s in labels:
        print(s.rjust(w), end="")
    print()

    # rows
    for P in pts:
        print(pt_str(P).rjust(w), end="")
        for Q in pts:
            R = ec_add(P, Q, p, A)
            print(pt_str(R).rjust(w), end="")
        print()

# ------------------------
# 5) Порядок точки ЭК + генераторы
# ------------------------

def ec_order(P, p, A):
    # порядок точки P: минимальный k>0, что kP = O
    if P is O:
        return 1
    k = 1
    R = P
    while R is not O:
        R = ec_add(R, P, p, A)
        k += 1
        if k > 10**7:
            # защита от вечного цикла (для учебных p не понадобится)
            return None
    return k

def ec_orders_table(p, A, B):
    if not is_prime(p):
        print("Ошибка: p должно быть простым.")
        return
    if ec_is_singular(p, A, B):
        print("Ошибка: кривая сингулярна (4A^3 + 27B^2 ≡ 0 mod p).")
        return

    pts = ec_points(p, A, B)
    N = len(pts)

    print("\nПорядки точек на ЭК")
    print(f"p={p}, A={A}, B={B}")
    print("|E(Fp)| =", N)
    print("Генератор группы точек: порядок = |E(Fp)| (обычно НЕ равно p-1)")
    print()

    # таблица: точка, порядок, генератор
    w = max(len(pt_str(P)) for P in pts) + 2
    print("P".ljust(w), "ord(P)".rjust(8), "генератор")
    print("-" * (w + 22))

    for P in pts:
        ordP = ec_order(P, p, A)
        gen = "*" if ordP == N else ""
        print(pt_str(P).ljust(w), str(ordP).rjust(8), "   ", gen)

# ------------------------
# Меню
# ------------------------

def main():
    while True:
        print("\n=== Практика 2.2 ===")
        print("1) Таблица умножения в Fp*")
        print("2) Порядки элементов в Fp* + генераторы")
        print("3) M-кратная композиция точки на ЭК (M*P) — пошагово")
        print("4) Таблица сложения точек ЭК")
        print("5) Порядки точек ЭК + генераторы")
        print("0) Выход")
        choice = input("Выбор: ").strip()

        if choice == "0":
            break

        if choice == "1":
            p = int(input("Введите простое p: "))
            mult_table_fp_star(p)

        elif choice == "2":
            p = int(input("Введите простое p: "))
            orders_table_fp_star(p)

        elif choice == "3":
            p = int(input("Введите простое p: "))
            A = int(input("Введите A (y^2 = x^3 + A*x + B): "))
            B = int(input("Введите B (y^2 = x^3 + A*x + B): "))
            if not is_prime(p):
                print("p должно быть простым.")
                continue
            if ec_is_singular(p, A, B):
                print("Кривая сингулярна, выберите другие A,B.")
                continue

            x = int(input("Введите x точки P: "))
            y = int(input("Введите y точки P: "))
            P = (x % p, y % p)
            if not ec_on_curve(P, p, A, B):
                print("Точка не лежит на кривой!")
                continue

            M = int(input("Введите M: "))
            ec_mul_verbose(M, P, p, A)

        elif choice == "4":
            p = int(input("Введите простое p: "))
            A = int(input("Введите A: "))
            B = int(input("Введите B: "))
            ec_add_table(p, A, B)

        elif choice == "5":
            p = int(input("Введите простое p: "))
            A = int(input("Введите A: "))
            B = int(input("Введите B: "))
            ec_orders_table(p, A, B)

        else:
            print("Неизвестный пункт меню.")

main()
