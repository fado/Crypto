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
