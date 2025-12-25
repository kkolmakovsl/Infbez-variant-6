n = 3
N = 2 ** n

L = 3
K = [6, 5, 0]   # K0, K1, K2

S = list(range(N))
j = 0

print("Task 4 (KSA):")
print(" i | j | S after swap")
print("-" * 35)

for i in range(N):
    j = (j + S[i] + K[i % L]) % N
    # swap
    S[i], S[j] = S[j], S[i]
    print(f"{i:>2} | {j} | {''.join(map(str, S))}")

print("\nИтоговая начальная перестановка S:", S)
