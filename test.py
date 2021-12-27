"""unittest for unit testing"""
import unittest
from main import Guess

#unit testing
class MyTestCase(unittest.TestCase):
    """Test Guess.check_guess()"""

    def test_guess_correct(self):
        """Test if guessed number equals generated number"""
        num = 10
        result = Guess.check_guess(self, num, 10)
        self.assertTrue(result)

    def test_guess_incorrect_less(self):
        """Test if guessed number is less than generated number"""
        num = 25
        result = Guess.check_guess(self, num, 20)
        self.assertFalse(result)

    def test_guess_incorrect_greater(self):
        """Test if guessed number is greater than generated number"""
        num = 25
        result = Guess.check_guess(self, num, 100)
        self.assertFalse(result)








if __name__ == '__main__':
    unittest.main()
