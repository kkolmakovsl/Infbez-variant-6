p = 59
Ca = 31
Cb = 13
Alpha = 58   # тройка
Beta = 7     # семерка
Gamma = 3    # туз

def egcd(a, b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0

def modinv(a, mod):
    g, x, y = egcd(a, mod)
    if g != 1:
        return None
    return x % mod

def card_name(v):
    if v == Alpha:
        return "Alpha (тройка)"
    if v == Beta:
        return "Beta (семерка)"
    if v == Gamma:
        return "Gamma (туз)"
    return "неизвестно"

print("Задача 4: Ментальный покер")
print(f"p={p}, Ca={Ca}, Cb={Cb}")
print(f"Карты: Alpha={Alpha}, Beta={Beta}, Gamma={Gamma}\n")

# Находим Da, Db: Ca*Da ≡ 1 (mod p-1), Cb*Db ≡ 1 (mod p-1)
Da = modinv(Ca, p - 1)
Db = modinv(Cb, p - 1)

print("Находим секретные обратные показатели:")
print("Da =", Da, "проверка:", (Ca * Da) % (p - 1))
print("Db =", Db, "проверка:", (Cb * Db) % (p - 1))
print()

deck = [Alpha, Beta, Gamma]
print("Исходные карты:", deck)

# 1) Алиса шифрует все карты
A = []
print("\n1) Алиса шифрует карты: A_i = card^Ca mod p")
for v in deck:
    enc = pow(v, Ca, p)
    A.append(enc)
    print(f"{v} -> {enc}")

print("Алиса отправляет Бобу:", A)

# 2) Боб шифрует поверх и тасует (для примера: разворот списка)
B = []
print("\n2) Боб шифрует поверх: B_i = A_i^Cb mod p")
for v in A:
    enc = pow(v, Cb, p)
    B.append(enc)
    print(f"{v} -> {enc}")

print("До тасовки у Боба:", B)

B_shuffled = [B[2], B[1], B[0]]  # фиксированная “тасовка” (чтобы было воспроизводимо)
print("После тасовки (пример):", B_shuffled)

# 3) Алиса берет первую карту (зашифрованную), чтобы получить ее — просит Боба снять его слой
alice_card_enc = B_shuffled[0]
print("\n3) Алиса выбирает карту (зашифр.):", alice_card_enc)

# Боб снимает свой слой: ^Db
alice_step = pow(alice_card_enc, Db, p)
print("Боб снимает свой слой: alice_step = enc^Db mod p =", alice_step)

# Алиса снимает свой слой: ^Da => получает карту
alice_card = pow(alice_step, Da, p)
print("Алиса снимает свой слой: alice_card = alice_step^Da mod p =", alice_card)
print("Карта Алисы:", alice_card, "-", card_name(alice_card))

# 4) Боб берет следующую карту, Алиса снимает свой слой, Боб снимает свой слой
bob_card_enc = B_shuffled[1]
print("\n4) Боб выбирает карту (зашифр.):", bob_card_enc)

bob_step = pow(bob_card_enc, Da, p)
print("Алиса снимает свой слой: bob_step = enc^Da mod p =", bob_step)

bob_card = pow(bob_step, Db, p)
print("Боб снимает свой слой: bob_card = bob_step^Db mod p =", bob_card)
print("Карта Боба:", bob_card, "-", card_name(bob_card))

# 5) Третья карта остается в прикупе (не раскрываем)
pri = B_shuffled[2]
print("\n5) Прикуп (остается зашифрованным, не раскрываем):", pri)
