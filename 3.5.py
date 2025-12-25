p = 7
roots = []
for g in range(2, p):
    vals = {pow(g, k, p) for k in range(1, p)}
    if len(vals) == p - 1:
        roots.append(g)

print("Подходящие g:", roots)
