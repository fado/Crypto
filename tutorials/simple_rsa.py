import argparse
import fractions
import logging
import random
from algorithms import extended_euclidean

log = logging.getLogger()


def generate_keys(prime_p, prime_q):
    """ Generate the public and private keys.

    :param prime_p, prime_q:  For our purposes, two small primes.
    :return: RSAPublicKey and RSAPrivateKey, derived from the passed-in primes.
    """

    # Calculate the product of the passed-in primes
    n = prime_p * prime_q

    # Calculate Euler's totient (phi) for the passed-in primes
    phi = (prime_p - 1) * (prime_q - 1)

    # Generate a public exponent
    while True:
        # 1 < e < phi
        pub_exp = random.randint(2, phi - 1)
        # gcd(phi, e) must equal 1
        if fractions.gcd(pub_exp, phi) == 1:
            break

    # Calculate the private exponent
    priv_exp = extended_euclidean(pub_exp, phi)
    log.debug("n: %s, phi: %s, pub_exp: %s, priv_exp: %s" % (n, phi, pub_exp, priv_exp))

    return RSAPublicKey(n, pub_exp), RSAPrivateKey(n, priv_exp)


def decrypt(message, priv_k):
    """ Decrypt the passed-in message.

    :param message: Message to be decrypted.
    :param priv_k: The RSA private key.
    :return: The plaintext corresponding to the passed-in ciphertext.
    """

    log.debug("DECRYPT: Private exponent: %s, private n: %s, message: %s" % (priv_k.priv_e, priv_k.n, message))
    return int(pow(message, priv_k.priv_e) % priv_k.n)


def encrypt(message, pub_k):
    """ Encrypt the passed-in message.

    :param message: The message to be encrypted.
    :param pub_k: The RSA public key.
    :return: The ciphertext corresponding to the passed-in message.
    """

    log.debug("ENCRYPT: Public exponent: %s, public n: %s, message: %s" % (pub_k.pub_e, pub_k.n, message))
    return int(pow(message, pub_k.pub_e) % pub_k.n)


class RSAPublicKey:
    """ RSA public key. """

    def __init__(self, n, pub_e):
        self.n = n
        self.pub_e = pub_e


class RSAPrivateKey:
    """ RSA private key. """

    def __init__(self, n, priv_e):
        self.n = n
        self.priv_e = priv_e


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

    # Select our primes
    prime_p = 3
    prime_q = 11

    # Generate our public and private keys
    pub_k, priv_k = generate_keys(prime_p, prime_q)
    log.debug("Public key: %s, %s" % (pub_k.n, pub_k.pub_e))
    log.debug("Private key: %s, %s" % (priv_k.n, priv_k.priv_e))

    # Select our messages
    message_1 = 4
    message_2 = 2

    # Encipher message_1
    ciphertext_1 = encrypt(message_1, pub_k)
    log.debug("Ciphertext of %s: %s" % (message_1, ciphertext_1))

    # Encipher message_2
    ciphertext_2 = encrypt(message_2, pub_k)
    log.debug("Ciphertext of %s: %s" % (message_2, ciphertext_2))

    # Encipher the product of message_1 and message_2
    ciphertext_3 = encrypt(message_1 * message_2, pub_k)
    log.debug("Ciphertext of %s: %s" % (message_1 * message_2, ciphertext_3))

    # The product of ciphertext_1 and ciphertext_2
    ciphertext_4 = ciphertext_1 * ciphertext_2
    log.debug("Product of ciphertexts: %s" % ciphertext_4)

    # Print the de-encryption of the product of message_1 and message_2 (ciphertext_3)
    print("D(E(4 * 2)): {0}".format(decrypt(ciphertext_3, priv_k)))
    # Print the de-encryption of the product of ciphertext_1 and ciphertext_2 (ciphertext_4)
    print("D(E(4) * E(2)): {0}".format(decrypt(ciphertext_4, priv_k)))
