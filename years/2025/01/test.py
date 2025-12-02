import unittest
from solutions import crack_safe_part1, crack_safe_part2

class TestCrackSafePart1(unittest.TestCase):

  def test_example_case(self):
    """Test the provided test case from file test.txt"""
    with open('test.txt', 'r') as f:
      rotations = f.read().strip().split("\n")
    self.assertEqual(crack_safe_part1(rotations), 3)

  def test_no_zeros(self):
    """Test case where we never land at zero"""
    rotations = ["R10", "L5"]
    self.assertEqual(crack_safe_part1(rotations), 0)

  def test_immediate_zero(self):
    """Test landing on 0 from starting position"""
    rotations = ["L50"]
    self.assertEqual(crack_safe_part1(rotations), 1)

  def test_wrapping_left(self):
    """Test when wrapping all the way around left"""
    rotations = ["L50", "L5"]
    self.assertEqual(crack_safe_part1(rotations), 1)

  def test_wrapping_right(self):
    """Test when wrapping all the way around right"""
    rotations = ["R50", "R5"]
    self.assertEqual(crack_safe_part1(rotations), 1)

  def test_multiple_zeros(self):
    """Test landing on 0 multiple times"""
    rotations = ['R50', 'L100', 'R100']
    self.assertEqual(crack_safe_part1(rotations), 3)
  
  def test_full_rotation(self):
    """Test full 100-click rotation returns to same position"""
    rotations = ['R100']
    self.assertEqual(crack_safe_part1(rotations), 0)
    
  def test_empty_rotations(self):
      """Test empty rotation list"""
      rotations = []
      self.assertEqual(crack_safe_part1(rotations), 0)


class TestCrackSafePart2(unittest.TestCase):

  def test_example_case_from_file(self):
    """Test example case from test file test.txt"""
    with open('test.txt', 'r') as f:
      rotations = f.read().strip().split("\n")
    self.assertEqual(crack_safe_part2(rotations), 6)

  def test_single_rotation_through_zero(self):
    """Test L68 from position 50 passes through 0 once"""
    rotations = ['L68']
    self.assertEqual(crack_safe_part2(rotations), 1)

  def test_end_exactly_on_zero(self):
      """Test ending on 0 counts as 1"""
      rotations = ['L50']
      self.assertEqual(crack_safe_part2(rotations), 1)

  def test_pass_through_and_end_on_zero(self):
      """Test passing through 0 and ending on 0"""
      rotations = ['L150']
      self.assertEqual(crack_safe_part2(rotations), 2)

  def test_multiple_wraps(self):
      """Test R1000 from position 50"""
      rotations = ['R1000']
      self.assertEqual(crack_safe_part2(rotations), 10)

  def test_no_zero_crossings(self):
      """Test rotation that doesn't cross 0"""
      rotations = ['R10']
      self.assertEqual(crack_safe_part2(rotations), 0)
  
  def test_left_rotation_no_wrap(self):
      """Test left rotation that doesn't wrap"""
      rotations = ['L30']
      self.assertEqual(crack_safe_part2(rotations), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)