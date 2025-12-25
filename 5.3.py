n = 94
a = 3

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True

def mod_pow_steps(base, exp, mod):
    res = 1
    base %= mod
    step = 0
    print(f"Вычисляем {base}^{exp} mod {mod} (быстрое возведение):")
    print("step | exp | bit | res(before)->res(after) | base(before)->base(after)")
    print("-"*78)
    while exp > 0:
        step += 1
        bit = exp % 2
        rb = res
        bb = base
        if bit == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        print(f"{step:>4} | {exp:>3} |  {bit}  | {rb:>3}->{res:>3}               | {bb:>3}->{base:>3}")
        exp //= 2
    return res

print("Задача 3: проверка псевдопростоты (Ферма)")
print(f"n={n}, a={a}")

g = gcd(a, n)
print("gcd(a,n) =", g)

if g != 1:
    print("Не псевдопростое: gcd(a,n) != 1")
else:
    if is_prime(n):
        print("n — простое, псевдопростым не считается (по определению).")
    else:
        r = mod_pow_steps(a, n - 1, n)
        print("\nПолучили:", r)
        if r == 1:
            print("n является псевдопростым по основанию a.")
        else:
            print("n НЕ является псевдопростым по основанию a.")
