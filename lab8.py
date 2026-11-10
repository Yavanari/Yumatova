import unittest
import math
def is_prime(n: int) -> bool:
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


class TestIsPrime(unittest.TestCase):

  def test_prime_numbers(self):
    for num in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97]:
      with self.subTest(num=num):
        self.assertTrue(is_prime(num) , f"Failed at {num}")

  def test_non_prime_numbers(self):
    for num in [0, 1, 4, 6, 8, 9, 10, 15, 21, 100]:
      with self.subTest(num=num):
        self.assertFalse(is_prime(num))

  def test_negative_numbers(self):
    for num in [-1, -5, -10, -97]:
      with self.subTest(num=num):
        self.assertFalse(
            is_prime(num))


if __name__ == '__main__':
  unittest.main()
