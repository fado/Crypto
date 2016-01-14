import random


def generate_key(security_parameter):
    key_length = security_parameter ** 2
    key = random.getrandbits(key_length)

    if key % 2 == 0:
        key += 1

    return key


def encrypt_bit(security_parameter, key, bit):
    random_bits = random.getrandbits(security_parameter)
    while random_bits % 2 != bit % 2:
        random_bits = random.getrandbits(security_parameter)

    return random_bits + (random.getrandbits(security_parameter ** 5) * key)


def decrypt(ciphertext, key):
    return (ciphertext % key) % 2


if __name__ == "__main__":
    security_parameter = 8
    key = generate_key(security_parameter)
    print(key)
    ciphertext_1 = encrypt_bit(security_parameter, key, 0)
    print(ciphertext_1)
    plaintext_1 = decrypt(ciphertext_1, key)
    print(plaintext_1)