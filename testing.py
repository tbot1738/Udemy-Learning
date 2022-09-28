import unittest
import mainForTesting


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        # Basically provide anything you want to before the test start like a vriable or smth
        print("About to start the function")
        return super().setUp()

    def test_do_smth(self):
        '''Test To Check the Answer/Result'''
        test_param = 5
        result = mainForTesting.do_smth(test_param)
        self.assertEqual(result, 10)

    def test_do_smth2(self):
        '''Test for ValueErrors'''
        test_param = "amogus sus O_o Rock Eyebrow raise sus mogs balls!!!"
        result = mainForTesting.do_smth(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)


if __name__ == "__main__":
    unittest.main()

'''Terminal Based Commands-:
python -m unittest
python -m unittest-v
'''
