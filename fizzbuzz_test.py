import unittest
import fizzbuzz

class TestStringMethods(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz.fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz.fizzbuzz(3), 'fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz.fizzbuzz(5), 'buzz')
        self.assertEqual(fizzbuzz.fizzbuzz(6), 'fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(15), 'fizzbuzz')

    def test_is_divisible(self):
        self.assertEqual(fizzbuzz.is_divisible(1, 3), False)
        self.assertEqual(fizzbuzz.is_divisible(2, 3), False)
        self.assertEqual(fizzbuzz.is_divisible(3, 3), True)
        self.assertEqual(fizzbuzz.is_divisible(3, 5), False)
        self.assertEqual(fizzbuzz.is_divisible(5, 5), True)

if __name__ == '__main__':
    unittest.main()