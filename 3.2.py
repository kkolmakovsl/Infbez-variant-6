import math

p = 97008000000
k = (p-1).bit_length()
m = math.isqrt(p-1)
if m*m < (p-1):
    m += 1

print("p =", p)
print("bit_length(p-1) =", k)
print("Fast pow worst-case multiplications =", 2*k)

print("Bruteforce (sequential) worst-case multiplications =", p-2)

print("BSGS m =", m)
print("BSGS approx multiplications ~ 2m =", 2*m)
