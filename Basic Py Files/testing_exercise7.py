import unittest
import exercise7


class TestGame(unittest.TestCase):
    def test_input_correct(self):
        '''Shows the Result of correct guess'''
        result = exercise7.game_guess(5, 5)
        self.assertTrue(result)

    def test_input_incorrect(self):
        '''Shows the Result of incorrect guess'''
        result = exercise7.game_guess(5, 0)
        self.assertFalse(result)


if __name__ == "__main__":
    print("Testing")
    unittest.main()
