a = 9
x = 952
p = 11

res = 1
base = a % p
step = 0

print(f"a={a}, x={x}, p={p}")
print(f"x (bin) = {x:b}")
print("step | x    | x%2 | res(before)->res(after) | base(before)->base(after)")
print("-"*78)

while x > 0:
    step += 1
    bit = x % 2

    res_before = res
    base_before = base

    if bit == 1:
        res = (res * base) % p

    base = (base * base) % p
    print(f"{step:>4} | {x:>4} |  {bit}  | {res_before:>2} -> {res:>2}              | {base_before:>2} -> {base:>2}")

    x //= 2

print("\nОтвет:", res)
