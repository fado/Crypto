import random
import math
import numpy
import string

# Constants
MODULO = 1024
SIGMA  = random.randint(math.sqrt(MODULO), 4096) # arbitrary upper bound

def keygen():
    a = random.randint(1, MODULO)
    s = numpy.random.normal(0, SIGMA, 1)[0]
    e = numpy.random.normal(0, SIGMA, 1)[0]
    b = (a * s + e) % MODULO

    return s, a, b


def encode(message):
    """ Encode the message into a real number.

    The bits of each letter are taken to be {0,1} coefficients in a polynomial.
    For example:
        1010011 => x + x^2 + x^6 + x^7
    """
    binary = ' '.join(format(ord(x), 'b') for x in message).split(" ")
    encoding = []

    for character in binary:
        total = 0
        for i in range(0,7):
            total += ( int(character[i]) * 2 ) ** i
        encoding.append(total)

    return encoding


def encrypt(encoding, a, b):
    r = numpy.random.normal(0, SIGMA, 1)[0]
    e1 = numpy.random.normal(0, SIGMA, 1)[0]
    e2  = numpy.random.normal(0, SIGMA, 1)[0]
    ciphertext = []

    for i in range(0, len(encoding)):
        u = (a * r + e1) % MODULO
        v = ((b * r + e2) + int(round(MODULO/2)) * encoding[i]) % MODULO
        ciphertext.append([u,v])

    return ciphertext


if __name__ == '__main__':
    print "KEYGEN:"
    s, a, b = keygen()
    print "Secret key: %s" % (s)
    print "Public key: %s, %s\n" % (a, b)

    print "ENCODING:"
    encoding = encode(string.ascii_letters)
    print encoding

    print "\nENCRYPTION:"
    encryption = encrypt(encoding, a, b)
    print encryption
