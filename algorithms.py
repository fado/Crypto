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
        quotient = old_r / r
        old_r, r = r, old_r - quotient * r
        old_t, t = t, old_t - quotient * t

    if t < 0:
        return modulus + t
    else:
        return t
