import unittest
import algorithms


class AlgorithmsTest(unittest.TestCase):
    def test_inverse_modulo(self):
        self.assertEqual(algorithms.extended_euclidean(67, 12), 28)

    def test_fix_negative_inverse_modulo(self):
        self.assertEqual(algorithms.extended_euclidean(19, 7), 11)

    # Based on http://goo.gl/0DD63h
    def test_not_relatively_prime_throws_exception(self):
        with self.assertRaises(ValueError) as context:
            algorithms.extended_euclidean(12, 24)
        self.assertTrue("Inputs are not relatively prime." in context.exception)
