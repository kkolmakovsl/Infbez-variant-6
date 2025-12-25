n = 115333

print("Задача 5: проверка простоты перебором")
print("n =", n)

if n < 2:
    print("Не простое (n < 2)")
else:
    d = 2
    is_prime = True

    while d * d <= n:
        if n % d == 0:
            is_prime = False
            print("Составное, делится на", d)
            break
        d += 1

    if is_prime:
        print("Простое")
