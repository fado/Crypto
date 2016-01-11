import math
from algorithms import extended_euclidean


def generate_keys(prime_p, prime_q):
    n = prime_p * prime_q
    phi = (prime_p - 1) * (prime_q - 1)
    pub_e = 3  # Chosen for the purposes of this demonstration
    priv_e = extended_euclidean(pub_e, phi)

    return RSAPublicKey(n, pub_e), RSAPrivateKey(n, priv_e)


def decrypt(message, priv_k):
    return int(math.pow(message, priv_k.priv_e) % priv_k.n)


def encrypt(message, pub_k):
    return int(math.pow(message, pub_k.pub_e) % pub_k.n)


class RSAPublicKey:

    def __init__(self, n, pub_e):
        self.n = n
        self.pub_e = pub_e


class RSAPrivateKey:

    def __init__(self, n, priv_e):
        self.n = n
        self.priv_e = priv_e


if __name__ == "__main__":
    prime_p = 3
    prime_q = 11
    pub_k, priv_k = generate_keys(prime_p, prime_q)

    message_1 = 4
    message_2 = 2

    ciphertext_1 = encrypt(message_1, pub_k)
    ciphertext_2 = encrypt(message_2, pub_k)
    ciphertext_3 = encrypt(message_1 * message_2, pub_k)
    ciphertext_4 = ciphertext_1 * ciphertext_2

    print("D(E(4 * 2)): {0}".format(decrypt(ciphertext_3, priv_k)))
    print("D(E(4) * E(2)): {0}".format(decrypt(ciphertext_4, priv_k)))
