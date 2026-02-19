import unittest
from main import addieren, subtrahieren, multiplizieren, dividieren

class test_taschenrechner(unittest.TestCase):
    def test_addieren(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)

    def test_subtrahieren(self):
        self.assertEqual(subtrahieren(5, 3), 2)
        self.assertEqual(subtrahieren(1, -1), 2)
        self.assertEqual(subtrahieren(0, 0), 0)
    
    def test_multiplizieren(self):
        self.assertEqual(multiplizieren(3, 2), 6)
        self.assertEqual(multiplizieren(-1, 1), -1)
        self.assertEqual(multiplizieren(0, 0), 0)
        
    def test_dividieren(self):
        self.assertEqual(dividieren(3, 2), 1.5)
        self.assertEqual(dividieren(-2, 0.5), -4)
        self.assertEqual(dividieren(-4, -2), 2)
        self.assertEqual(dividieren(-3, 0), None)
        self.assertEqual(dividieren(0, 0), None)

if __name__ == '__main__':
    unittest.main()
