N = 56000000000

def ln_int(n, terms=20):
    # ln(n) без import math, через разложение:
    # n = m * 2^e, m in [1,2), ln(n)=ln(m)+e*ln2
    LN2 = 0.6931471805599453
    if n <= 0:
        raise ValueError("n must be > 0")

    e = n.bit_length() - 1
    m = n / (1 << e)  # 1 <= m < 2

    y = (m - 1) / (m + 1)
    y2 = y * y

    s = 0.0
    p = y
    for k in range(terms):
        s += p / (2 * k + 1)
        p *= y2

    return 2.0 * s + e * LN2

lnN = ln_int(N, terms=20)

est1 = N / lnN
est2 = N / (lnN - 1)

print("Задача 5: оценка π(N)")
print("N =", N)
print("ln(N) ≈", lnN)
print("π(N) ≈ N/ln(N) =", int(est1))
print("π(N) ≈ N/(ln(N)-1) =", int(est2))
