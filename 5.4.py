nums = [30, 34, 49, 64, 98]

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True

print("Задача 4: проверка на простоту")
for i, v in enumerate(nums, start=1):
    if is_prime(v):
        print(f"x{i}={v} -> простое")
    else:
        print(f"x{i}={v} -> составное")
