import unittest
from main import addieren
from main import subtrahieren

class TestTaschenrechner(unittest.TestCase):
    def test_addieren(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)

    def test_subtrahieren(self):
        self.assertEqual(subtrahieren(5, 3), 2)
        self.assertEqual(subtrahieren(1, -1), 2)
        self.assertEqual(subtrahieren(0, 0), 0)
        
if __name__ == '__main__':
    unittest.main()