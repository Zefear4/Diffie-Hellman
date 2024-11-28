import random


def get_power_mod(num, power, mod):
    result = 1
    num = num % mod
    while power > 0:
        if power % 2 == 1:
            result = (result * num) % mod
        power = power >> 1
        num = (num * num) % mod
    return result

def find_greatest_common_divisor(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def is_prime(n, iteration):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(iteration):
        a = random.randint(2, n - 2)
        if find_greatest_common_divisor(a, n) != 1:
            return False
        if get_power_mod(a, n - 1, n) != 1: # Тест Миллера-Рабина
            return False
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num, 5) and is_prime(int((num-1)/2), 5):
            return num

def primitive_root(n):
    for root in range(2, n):
        powers = set()
        for i in range(1, n):
            powers.add(pow(root, i, n))
        if len(powers) == n - 1:
            return root

def generate_private_key(p):
    return random.randint(2, p - 1)

def generate_public_key(g, private_key, p):
    return get_power_mod(g, private_key, p)

def genetate_common_key(public_key, private_key, p):
    return get_power_mod(public_key, private_key, p)

def main():
    p = generate_prime(10)
    g = primitive_root(p)
    user1_private_key = generate_private_key(p)
    user2_private_key = generate_private_key(p)
    user1_public_key = generate_public_key(g, user1_private_key, p)
    user2_public_key = generate_public_key(g, user2_private_key, p)
    user1_common_key = genetate_common_key(user2_public_key, user1_private_key,
    p)
    user2_common_key = genetate_common_key(user1_public_key, user2_private_key,
    p)
    print("Надежное простое число p:", p)
    print("Первообразный корень g:", g)
    print("Закрытый ключ Пользователя1:", user1_private_key)
    print("Закрытый ключ Пользователя2", user2_private_key)
    print("Открытый ключ Пользователя1:", user1_public_key)
    print("Открытый ключ Пользователя1:", user2_public_key)
    print("Общий ключ Пользователя1", user1_common_key)
    print("Общий ключ Пользователя2", user2_common_key)

main()