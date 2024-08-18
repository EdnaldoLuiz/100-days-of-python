import unittest

def soma(a, b):
    return a + b

class Testes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)
        self.assertEqual(soma(2, 2), 4)
        self.assertEqual(soma(3, 2), 5)

if __name__ == '__main__':
    unittest.main()