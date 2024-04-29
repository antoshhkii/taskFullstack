import unittest
from main import unique_elements, is_prime, prime_numbers, Point, sort_strings

class TestMainFunctions(unittest.TestCase):
    def test_unique_elements(self):
        self.assertEqual(unique_elements([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(unique_elements([1, 1, 1, 1]), [1])
        self.assertEqual(unique_elements([]), [])

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

    def test_prime_numbers(self):
        self.assertEqual(prime_numbers(1, 10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers(10, 20), [11, 13, 17, 19])
        self.assertEqual(prime_numbers(20, 30), [23, 29])

    def test_point_distance(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)

    def test_sort_strings(self):
        strings = ["apple", "banana", "cherry", "date"]
        asc_sorted, desc_sorted = sort_strings(strings)
        self.assertEqual(asc_sorted, ["date", "apple", "banana", "cherry"])
        self.assertEqual(desc_sorted, ["cherry", "banana", "apple", "date"])

if __name__ == '__main__':
    unittest.main()
