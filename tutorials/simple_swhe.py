import random


def generate_key(security_parameter):
    """ Generate a random n bit key, where n is the secuity parameter.

    :param security_parameter:
    :return: a random n bit integer, where n is the security parameter
    """
    key_length = security_parameter ** 2
    key = random.getrandbits(key_length)

    # Key needs to be an odd number.
    if key % 2 == 0:
        key += 1

    return key


def encrypt_bit(security_parameter, key, bit):
    """ Encrypt the passed-in bit.

    :param security_parameter:
    :param key:
    :param bit: a single-bit
    :return: a ciphertext corresponding to the passed-in bit
    """
    random_bits = random.getrandbits(security_parameter)
    while random_bits % 2 != bit % 2:
        random_bits = random.getrandbits(security_parameter)

    return random_bits + (random.getrandbits(security_parameter ** 5) * key)


def decrypt(ciphertext, key):
    """ Decrypt the passed-in ciphertext using the passed-in key

    :param ciphertext: Ciphertext to be decrypted
    :param key: Key with which to decrypt the ciphertext
    :return: Plaintext corresponding to the passed-in ciphertext
    """
    return (ciphertext % key) % 2


if __name__ == "__main__":
    security_parameter = 8
    key = generate_key(security_parameter)

    ciphertext_1 = encrypt_bit(security_parameter, key, 0)
    plaintext_1 = decrypt(ciphertext_1, key)

