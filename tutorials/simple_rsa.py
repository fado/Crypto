import math

from algorithms import extended_euclidean


def main():
    # STEP 1: Select two primes p and q, and multiply them together.
    prime_p = 3
    prime_q = 11
    modulus = prime_p * prime_q

    # STEP 2: Calculate Euler's totient for the modulus. Remember that this is easy in
    #         when p and q are both known primes. In that case we can simply say that
    #         phi = (p - 1)(q - 1) = (3 - 1)(11 - 1) = (2 * 10) = 20.
    phi = 20

    # STEP 3: Select a public exponent that is relatively prime to phi.
    public_exponent = 3

    # STEP 4: Calculate the private exponent. An implementation of the extended Euclidean
    #         algorithm has been included to make this easier.
    private_exponent = extended_euclidean(public_exponent, phi)

    # STEP 5: We select two messages that we want to encrypt.
    message_1 = 4
    message_2 = 2

    # STEP 6: We can now demonstrate the multiplicative homomorphism in RSA. If RSA is in
    #         fact multiplicatively homomorphic, the result of encrypting 4 * 2 should be
    #         the same as encrypting 4, encrypting 2 and multiplying those ciphertexts
    #         together.
    ciphertext_1 = encrypt(message_1, public_exponent, modulus)
    ciphertext_2 = encrypt(message_2, public_exponent, modulus)
    ciphertext_3 = encrypt(message_1 * message_2, public_exponent, modulus)
    ciphertext_4 = ciphertext_1 * ciphertext_2

    print("D(E(4 * 2)): {0}".format(decrypt(ciphertext_3, private_exponent, modulus)))
    print("D(E(4) * E(2)): {0}".format(decrypt(ciphertext_4, private_exponent, modulus)))


"""
Our encryption and decryption methods are identical. The only difference is which
exponent we pass to them. In the case of encryption, we pass the public exponent from
the public key. In the case of decryption, we pass the private exponent from the private
key. However, for the sake of clarity in this example, we will create two methods to
avoid confusion.
"""


def decrypt(message, private_exponent, modulus):
    """ Encrypts the given message.

    Raises the message to the exponent, mod n.

    :param message: Message to be encrypted.
    :param private_exponent: Public exponent from the RSA public key.
    :param modulus: Modulus from the RSA key.
    :return: The encrypted message.
    """
    return int(math.pow(message, private_exponent) % modulus)


def encrypt(message, public_exponent, modulus):
    """ Encrypts the given message.

    Raises the message to the exponent, mod n.

    :param message: Message to be encrypted.
    :param public_exponent: Public exponent from the RSA public key.
    :param modulus: Modulus from the RSA key.
    :return: The encrypted message.
    """
    return int(math.pow(message, public_exponent) % modulus)


if __name__ == "__main__":
    main()
