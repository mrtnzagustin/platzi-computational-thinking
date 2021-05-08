import unittest

def sum_custom(a, b):
    return a + b

class CajaNegraTest(unittest.TestCase):

    def test_sum_positive(self):
        num_1 = 10
        num_2 = 5

        result = sum_custom(num_1, num_2)

        self.assertEqual(result, 15)
        
    def test_sum_negatives(self):
        num_1 = -10
        num_2 = -7

        result = sum_custom(num_1, num_2)

        self.assertEqual(result, -17)

if __name__ == '__main__':
    unittest.main()