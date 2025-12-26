# Практическое задание 4 — Блочный шифр (Feistel) (без import)

def read_file_bytes(path):
    with open(path, "rb") as f:
        return f.read()

def write_file_bytes(path, data):
    with open(path, "wb") as f:
        f.write(data)

def u32(x):
    return x & 0xFFFFFFFF

def rotl32(x, r):
    x = u32(x)
    r = r & 31
    return u32((x << r) | (x >> (32 - r)))

def feistel_f(r, k):
    x = u32(r ^ k)
    x = rotl32(x, 7)
    x = u32(x + 0x9E3779B9)
    x = rotl32(x, 11)
    return x

def key_to_u32(key_bytes):
    acc = 0
    for i, b in enumerate(key_bytes):
        acc = u32(acc + (b << (i % 24)))
    return acc

def feistel_subkeys(key_bytes, rounds):
    x = key_to_u32(key_bytes)
    keys = []
    for _ in range(rounds):
        x = u32(x * 1664525 + 1013904223)
        keys.append(x)
    return keys

def feistel_encrypt_block(block8, subkeys):
    L = int.from_bytes(block8[0:4], "big")
    R = int.from_bytes(block8[4:8], "big")
    for k in subkeys:
        L, R = R, u32(L ^ feistel_f(R, k))
    return L.to_bytes(4, "big") + R.to_bytes(4, "big")

def feistel_decrypt_block(block8, subkeys):
    L = int.from_bytes(block8[0:4], "big")
    R = int.from_bytes(block8[4:8], "big")
    for k in reversed(subkeys):
        L, R = u32(R ^ feistel_f(L, k)), L
    return L.to_bytes(4, "big") + R.to_bytes(4, "big")

def pkcs7_pad(data, block_size):
    pad = block_size - (len(data) % block_size)
    if pad == 0:
        pad = block_size
    return data + bytes([pad]) * pad

def pkcs7_unpad(data, block_size):
    if len(data) == 0 or len(data) % block_size != 0:
        return None
    pad = data[-1]
    if pad < 1 or pad > block_size:
        return None
    for i in range(1, pad + 1):
        if data[-i] != pad:
            return None
    return data[:-pad]

def encrypt_file():
    in_path = input("Входной файл: ").strip()
    out_path = input("Выходной файл: ").strip()
    key_str = input("Ключ (строка): ")
    key_bytes = key_str.encode("utf-8")
    if len(key_bytes) == 0:
        print("ОШИБКА: ключ пустой")
        return

    rounds = 16
    block = 8
    subkeys = feistel_subkeys(key_bytes, rounds)

    data = read_file_bytes(in_path)
    data = pkcs7_pad(data, block)

    out = bytearray()
    for i in range(0, len(data), block):
        out += feistel_encrypt_block(data[i:i+block], subkeys)

    write_file_bytes(out_path, bytes(out))
    print("Зашифровано:", out_path)

def decrypt_file():
    in_path = input("Входной файл: ").strip()
    out_path = input("Выходной файл: ").strip()
    key_str = input("Ключ (строка): ")
    key_bytes = key_str.encode("utf-8")
    if len(key_bytes) == 0:
        print("ОШИБКА: ключ пустой")
        return

    rounds = 16
    block = 8
    subkeys = feistel_subkeys(key_bytes, rounds)

    data = read_file_bytes(in_path)
    if len(data) % block != 0:
        print("ОШИБКА: размер шифртекста не кратен 8")
        return

    out = bytearray()
    for i in range(0, len(data), block):
        out += feistel_decrypt_block(data[i:i+block], subkeys)

    unp = pkcs7_unpad(bytes(out), block)
    if unp is None:
        print("ОШИБКА: неверный ключ или данные повреждены")
        return

    write_file_bytes(out_path, unp)
    print("Расшифровано:", out_path)

def main():
    while True:
        print("\n=== Практическое задание 4 ===")
        print("1) Зашифровать файл")
        print("2) Расшифровать файл")
        print("0) Выход")
        ch = input("Выбор: ").strip()

        if ch == "0":
            break
        elif ch == "1":
            encrypt_file()
        elif ch == "2":
            decrypt_file()
        else:
            print("Неизвестный пункт.")

main()
