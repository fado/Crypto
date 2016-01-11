import math
import random
from algorithms import extended_euclidean


def generate_keys(prime_p, prime_q):
    n = prime_p * prime_q
    g = n + 1
    lmda = (prime_p - 1) * (prime_q - 1)
    mu = extended_euclidean(lmda, n)
    return PallierPublicKey(n, g), PallierPrivateKey(lmda, mu)


def encrypt(message, pub_k):
    r = random.randint(1, pub_k.n)
    return math.pow(pub_k.g, message) * math.pow(r, pub_k.n) % math.pow(pub_k.n, 2)


def decrypt(message, priv_k, pub_k):
    u = math.pow(message, priv_k.lmda) % math.pow(pub_k.n, 2)
    l = (u - 1) / pub_k.n
    return l * priv_k.mu % pub_k.n


class PallierPublicKey:
    """ Paillier public key. """

    def __init__(self, n, g):
        self.n = n
        self.g = g


class PallierPrivateKey:
    """ Paillier private key. """

    def __init__(self, lmda, mu):
        self.lmda = lmda
        self.mu = mu

if __name__ == "__main__":
    # Generate the keys based on primes that we will supply
    public_key, private_key = generate_keys(3, 5)

    # Select the two messages we want to encrypt
    message_1 = 2
    message_2 = 4

    ciphertext_1 = encrypt(message_1, public_key)
    ciphertext_2 = encrypt(message_2, public_key)
    ciphertext_3 = encrypt(message_1 + message_2, public_key)
    ciphertext_4 = ciphertext_1 * ciphertext_2

    print("D(E(4 + 2)): {0}".format(decrypt(ciphertext_3, private_key, public_key)))
    print("D(E(4) * E(2)): {0}".format(decrypt(ciphertext_4, private_key, public_key)))
