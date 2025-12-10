import unittest
from solutions import (
    sanitize_ids, 
    is_sequence_repeated_twice, 
    sum_invalid_ids_part1,
    solve_part1
)


class TestInvalidIDsPart1(unittest.TestCase):
    
    def test_sanitize_ids(self):
        """Test parsing first and last number in ID range"""
        number_range = '11-22'
        first, last = sanitize_ids(number_range)
        self.assertEqual(first, 11)
        self.assertEqual(last, 22)

    def test_is_sequence_repeated_twice_valid(self):
        """Test identifying numbers that are sequences repeated exactly twice"""
        self.assertTrue(is_sequence_repeated_twice(11))
        self.assertTrue(is_sequence_repeated_twice(22))
        self.assertTrue(is_sequence_repeated_twice(55))
        self.assertTrue(is_sequence_repeated_twice(99))
        self.assertTrue(is_sequence_repeated_twice(1010))
        self.assertTrue(is_sequence_repeated_twice(6464))
        self.assertTrue(is_sequence_repeated_twice(123123))
        self.assertTrue(is_sequence_repeated_twice(1188511885))
        self.assertTrue(is_sequence_repeated_twice(222222))
        self.assertTrue(is_sequence_repeated_twice(446446))
        self.assertTrue(is_sequence_repeated_twice(38593859))

    def test_is_sequence_repeated_twice_invalid(self):
        """Test identifying numbers that are NOT sequences repeated exactly twice"""
        self.assertFalse(is_sequence_repeated_twice(12))
        self.assertFalse(is_sequence_repeated_twice(13))
        self.assertFalse(is_sequence_repeated_twice(112))
        self.assertFalse(is_sequence_repeated_twice(123))
        self.assertFalse(is_sequence_repeated_twice(1221))
        self.assertFalse(is_sequence_repeated_twice(101))
        self.assertFalse(is_sequence_repeated_twice(111))

    def test_sum_invalid_ids_example_ranges(self):
        """Test summing invalid IDs from example ranges"""
        self.assertEqual(sum_invalid_ids_part1(11, 22), 33)
        self.assertEqual(sum_invalid_ids_part1(95, 115), 99)
        self.assertEqual(sum_invalid_ids_part1(998, 1012), 1010)
        self.assertEqual(sum_invalid_ids_part1(1698522, 1698528), 0)

    def test_full_example_part1(self):
        """Test the full example from part 1 using test.txt"""
        result = solve_part1('test.txt')
        self.assertEqual(result, 1227775554)


if __name__ == '__main__':
    unittest.main()