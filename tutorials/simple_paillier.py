import argparse
import logging
import random
from algorithms import extended_euclidean
from tutorials.keys import PallierPrivateKey, PallierPublicKey

log = logging.getLogger()


def generate_keys(prime_p, prime_q):
    """ Generate a public and private key.

    To simplify the key generation process, we assume that the primes are of
    equivalent length. (Maybe implement the more complicated key generation algorithm
    in the future?)

    :param prime_p, prime_q: For our purposes, two small primes of equivalent length.
    :return: PaillierPublicKey and PaillierPrivateKey derived from the passed-in primes.
    """

    # Calculate the product of the passed-in primes.
    n = prime_p * prime_q

    # Calculate g = n + 1
    g = n + 1

    # Calculate lambda as phi of n (Euler's totient)
    lmda = (prime_p - 1) * (prime_q - 1)

    # Calculate mu as the multiplicative inverse of phi of n mod n
    mu = extended_euclidean(lmda, n)

    return PallierPublicKey(n, g), PallierPrivateKey(lmda, mu)


def encrypt(message, pub_k):
    """ Encrypt the passed-in message.

    :param message: The message to be encrypted.
    :param pub_k: The Paillier public key.
    :return: The ciphertext corresponding to the passed-in message.
    """

    # Generate a ranadom noise 1 <= r <= n
    r = random.randint(1, pub_k.n)

    # Encrypt with g^m * r^n % n^2
    return ((pub_k.g ** message) * (r ** pub_k.n)) % (pub_k.n ** 2)


def decrypt(message, priv_k, pub_k):
    """ Decrypt the passed-in message.

    :param message: The message to be decrypted.
    :param priv_k: The Paillier private key.
    :param pub_k: The Paillier public key.
    :return: The plaintext corresponding to the passed-in message.
    """

    # Calculate u as m^lmda % n^2
    u = (message ** priv_k.lmda) % (pub_k.n ** 2)

    # Calculate L
    l = (u - 1) / pub_k.n

    # Decrypt with L * u % n
    return l * priv_k.mu % pub_k.n


def init_logging():
    """ Initialise the logger with our custom format string. """

    formatter = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: "
                                  "%(message)s")
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    log.addHandler(consoleHandler)

if __name__ == "__main__":
    # Check for runtime arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help="Show "
                        "debug messages.")
    args = parser.parse_args()

    # Init some logging to make our lives easier
    init_logging()

    # Check if we want any debug messages
    if args.debug:
        log.setLevel(logging.DEBUG)

    # Generate the keys based on primes that we will supply
    pub_k, priv_k = generate_keys(79, 73)
    log.debug("Public key: n=%s, g=%s" % (pub_k.n, pub_k.g))
    log.debug("Private key: mu=%s, lmda=%s" % (priv_k.mu, priv_k.lmda))

    # Select the two messages we want to encrypt
    message_1 = 2
    message_2 = 4

    # Encipher message_1
    ciphertext_1 = encrypt(message_1, pub_k)
    log.debug("Ciphertext of %s: %s" % (message_1, ciphertext_1))

    # Encipher message_2
    ciphertext_2 = encrypt(message_2, pub_k)
    log.debug("Ciphertext of %s: %s" % (message_2, ciphertext_2))

    # Encipher the sum of message_1 and message_2
    ciphertext_3 = encrypt(message_1 + message_2, pub_k)
    log.debug("Ciphertext of %s: %s" % (message_1 * message_2, ciphertext_3))

    # The product of ciphertext_1 and ciphertext_2
    ciphertext_4 = ciphertext_1 * ciphertext_2
    log.debug("Product of ciphertexts: %s" % ciphertext_4)

    # Print the de-encryption of the sum of message_1 and message_2 (ciphertext_3)
    print("D(E(4 + 2)): {0}".format(decrypt(ciphertext_3, priv_k, pub_k)))
    # Print the de-encryption of the product of ciphertext_1 and ciphertext_2 (ciphertext_4)
    print("D(E(4) * E(2)): {0}".format(decrypt(ciphertext_4, priv_k, pub_k)))
