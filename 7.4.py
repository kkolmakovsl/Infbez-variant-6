a = 4
b = 6

print("Задача 4: НОК перебором")
print("a =", a, "b =", b)

lcm = None
k = 1
while True:
    if k % a == 0 and k % b == 0:
        lcm = k
        break
    k += 1

print("НОК =", lcm)
