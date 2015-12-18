from fractions import gcd


def extended_euclidean(modulus, integer):
    """ Finds the inverse modulo of b, mod a.

    Based on the pseudocode taken from
    http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode

    :param modulus: The modulus.
    :param integer: The number for which the inverse modulo is to be computed.
    """
    if gcd(modulus, integer) != 1:
        raise ValueError("Inputs are not relatively prime.")

    t, old_t = 1, 0
    r, old_r = integer, modulus

    while r != 1:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_t, t = t, old_t - quotient * t

    if t < 0:
        return modulus + t
    else:
        return t


def eulers_totient(integer):
    """ Naieve (read: simple and inefficient) algorithm to compute Euler's totient
    for a given integer.  Returns the number of positive integers less than integer
    and relatively prime to integer.

    :param integer: The integer for which we wish to compute Euler's totient.
    :return: Euler's totient for the passed-in integer.
    """
    # TO-DO: Test for primality.

    if integer <= 0:
        return 0

    totient = 0

    for i in range(0, integer - 1):
        if gcd(i, integer) == 1:
            totient += 1

    return totient
