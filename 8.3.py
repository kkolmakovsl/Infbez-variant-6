p = 20477000000

def isqrt_floor(n):
    # целая sqrt(n) вниз (Ньютон), без import
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def isqrt_ceil(n):
    r = isqrt_floor(n)
    if r * r < n:
        r += 1
    return r

print("Задача 3: оценка числа умножений")
print("p =", p)

# Прямая функция: fast pow (square-and-multiply)
bits = (p - 1).bit_length()
worst_fast_pow = 2 * bits  # худший случай popcount ~ bits
best_fast_pow = bits + 1   # примерно: один бит '1'
print("\nПрямая функция a^x mod p (быстрое возведение):")
print("bit_length(p-1) =", bits)
print("оценка умножений: от", best_fast_pow, "до", worst_fast_pow)

# Обратная функция: перебор (последовательным домножением)
bruteforce = p - 2
print("\nОбратная функция (полный перебор, последовательное домножение):")
print("умножений (худший случай) =", bruteforce)

# Обратная функция: BSGS
m = isqrt_ceil(p - 1)
bsgs_mult = 2 * m
print("\nОбратная функция (Шаг младенца — Шаг великана, BSGS):")
print("m = ceil(sqrt(p-1)) =", m)
print("примерная оценка умножений ~ 2m =", bsgs_mult)
