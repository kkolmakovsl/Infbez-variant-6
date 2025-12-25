n = 3
N = 2 ** n

S_str = "12576304"                
S = [int(ch) for ch in S_str]      
if sorted(S) != list(range(N)):
    raise ValueError("S должна быть перестановкой чисел 0..7")

i = 0
j = 0
out = []

print("Task 3 (PRGA):")
print("step | i | j | t | z=S[t] | S after swap")
print("-" * 60)

for step in range(1, 8 + 1):
    i = (i + 1) % N
    j = (j + S[i]) % N

    # swap
    S[i], S[j] = S[j], S[i]

    t = (S[i] + S[j]) % N
    z = S[t]
    out.append(z)

    print(f"{step:>4} | {i} | {j} | {t} |   {z:>3}  | {''.join(map(str, S))}")

print("\nСгенерированные 8 чисел:", out)
