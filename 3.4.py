p = 23
g = 14
Xa, Xb, Xc = 8, 22, 18

Ya = pow(g, Xa, p)
Yb = pow(g, Xb, p)
Yc = pow(g, Xc, p)

Kab = pow(Yb, Xa, p)
Kac = pow(Yc, Xa, p)
Kbc = pow(Yc, Xb, p)

print("Ya =", Ya, "Yb =", Yb, "Yc =", Yc)
print("K_ab =", Kab)
print("K_ac =", Kac)
print("K_bc =", Kbc)
