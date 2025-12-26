# Практическое задание 2 — Энтропия файла (без import)

def read_file_bytes(path):
    with open(path, "rb") as f:
        return f.read()

def ln_int(n, terms=24):
    LN2 = 0.6931471805599453
    if n <= 0:
        raise ValueError("n must be > 0")

    e = n.bit_length() - 1
    m = n / (1 << e)  # 1 <= m < 2

    y = (m - 1) / (m + 1)
    y2 = y * y

    s = 0.0
    p = y
    for k in range(terms):
        s += p / (2 * k + 1)
        p *= y2

    return 2.0 * s + e * LN2

def log2_float(x):
    LN2 = 0.6931471805599453
    return ln_int(x) / LN2

def freq_bytes(data):
    f = [0] * 256
    for b in data:
        f[b] += 1
    return f

def show_frequencies(path):
    data = read_file_bytes(path)
    freq = freq_bytes(data)
    total = len(data)

    print("\n[Практическое 2] Частоты байтов")
    print("Файл:", path)
    print("Всего байт:", total)
    print("Ненулевые частоты (байт -> count):")
    for i in range(256):
        if freq[i] != 0:
            print(f"{i:3d} -> {freq[i]}")

def entropy(path):
    data = read_file_bytes(path)
    freq = freq_bytes(data)
    total = len(data)

    print("\n[Практическое 2] Энтропия")
    print("Файл:", path)
    print("Всего байт:", total)

    if total == 0:
        print("Файл пустой. Энтропия = 0")
        return

    H = 0.0
    for c in freq:
        if c > 0:
            p = c / total
            H -= p * log2_float(p)

    print("Энтропия H (бит/символ) ≈", H)

def main():
    while True:
        print("\n=== Практическое задание 2 ===")
        print("1) Показать частоты байтов")
        print("2) Посчитать энтропию файла")
        print("0) Выход")
        ch = input("Выбор: ").strip()

        if ch == "0":
            break
        elif ch == "1":
            path = input("Путь к файлу: ").strip()
            show_frequencies(path)
        elif ch == "2":
            path = input("Путь к файлу: ").strip()
            entropy(path)
        else:
            print("Неизвестный пункт.")

main()
