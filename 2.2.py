a = 1228
b = 2746
c = 3017
x = 2422  # x0

nums = []
for i in range(10):
    x = (a * x + b) % c
    nums.append(x)
    print(f"x{i+1} = {x}")

print("Список 10 чисел:", nums)
