# Практическое задание 3 — Вернам + RC4 (без import)

def read_file_bytes(path):
    with open(path, "rb") as f:
        return f.read()

def write_file_bytes(path, data):
    with open(path, "wb") as f:
        f.write(data)

def lcg_bytes(size, seed):
    a = 1103515245
    c = 12345
    m = 1 << 31
    x = seed % m
    out = bytearray()
    for _ in range(size):
        x = (a * x + c) % m
        out.append(x & 0xFF)
    return bytes(out)

def xor_bytes(a, b):
    n = min(len(a), len(b))
    out = bytearray(n)
    for i in range(n):
        out[i] = a[i] ^ b[i]
    return bytes(out)

# ----- Вернам -----

def vernam_file(pt_path, key_path, out_path):
    pt = read_file_bytes(pt_path)
    key = read_file_bytes(key_path)
    if len(key) < len(pt):
        print("ОШИБКА: ключ короче текста (ключ должен быть >= длины текста)")
        return
    ct = xor_bytes(pt, key)
    write_file_bytes(out_path, ct)
    print("Готово:", out_path)

# ----- RC4 -----

def rc4_ksa(key_bytes):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_prga(S, n):
    i = 0
    j = 0
    out = bytearray(n)
    for t in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        out[t] = k
    return bytes(out)

def rc4_file(in_path, out_path, key_str):
    data = read_file_bytes(in_path)
    key_bytes = key_str.encode("utf-8")
    if len(key_bytes) == 0:
        print("ОШИБКА: пустой ключ")
        return
    S = rc4_ksa(key_bytes)
    ks = rc4_prga(S, len(data))
    out = xor_bytes(data, ks)
    write_file_bytes(out_path, out)
    print("Готово:", out_path)

def main():
    while True:
        print("\n=== Практическое задание 3 ===")
        print("1) Сгенерировать ключ-файл (LCG)")
        print("2) Вернам (XOR) файл + ключ-файл")
        print("3) RC4 (шифровать/расшифровать файл)")
        print("0) Выход")
        ch = input("Выбор: ").strip()

        if ch == "0":
            break

        elif ch == "1":
            out_path = input("Куда сохранить ключ (путь): ").strip()
            size = int(input("Размер ключа (байт): ").strip())
            seed = int(input("Seed: ").strip())
            key = lcg_bytes(size, seed)
            write_file_bytes(out_path, key)
            print("Ключ создан:", out_path)

        elif ch == "2":
            pt_path = input("Файл текста (путь): ").strip()
            key_path = input("Файл ключа (путь): ").strip()
            out_path = input("Куда сохранить результат (путь): ").strip()
            vernam_file(pt_path, key_path, out_path)

        elif ch == "3":
            in_path = input("Входной файл: ").strip()
            out_path = input("Выходной файл: ").strip()
            key = input("Ключ (строка): ")
            rc4_file(in_path, out_path, key)

        else:
            print("Неизвестный пункт.")

main()
