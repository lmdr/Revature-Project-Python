import unittest
from main import Guess

#unit testing
class MyTestCase(unittest.TestCase):

    def test_guess_correct(self):
        num = 10
        result = Guess.check_guess(num, 10)
        self.assertTrue(result)

    def test_guess_incorrect_less(self):
        num = 25
        result = Guess.check_guess(num, 20)
        self.assertFalse(result)

    def test_guess_incorrect_greater(self):
        num = 25
        result = Guess.check_guess(num, 100)
        self.assertFalse(result)








if __name__ == '__main__':
    unittest.main()
